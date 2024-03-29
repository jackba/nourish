from django.views.generic import DetailView, UpdateView, ListView
from nourish.models import EventGroup, Event, GroupUser, Meal, MealInvite, EventUser
from nourish.forms import EventForm, EventGroupHostForm, EventInviteDayForm, EventInviteMealForm
from nourish.forms.event import EventGroupHostFeaturesForm, EventGroupHostForm
from nourish.forms.register import RegistrationStubForm
from nourish.forms.group import GroupForm, GroupFBForm
from django.shortcuts import get_object_or_404, redirect
from datetime import timedelta
from fbcanvas.views import HybridCanvasView
from nourish.views.register.host import EventHostRegisterView
from django.forms.formsets import formset_factory
from django.core.exceptions import PermissionDenied
import json

import sys
from pprint import pformat
import pprint

class EventHostInviteView(EventHostRegisterView):
    template_name = 'nourish/EventHostInviteView.html'

    def get_post_formsets(self, request):
        formsets = super(EventHostInviteView, self).get_post_formsets(request)

        day_factory = formset_factory(EventInviteDayForm, extra=0)
        meal_factory = formset_factory(EventInviteMealForm, extra=0)

        formsets['day_formset'] = day_factory(request.POST, prefix='days')
        formsets['meal_formset'] = meal_factory(request.POST, prefix='meals')

        return formsets

        (dates, day_initial, meal_initial) = self.get_meals(host_eg, guest_eg, 'manage' in self.request.GET)
        dates = self.get_meal_dates(dates, day_formset, meal_formset)

    def formsets_valid(self, formsets):
        (host_eg, guest_eg) = self.get_egs()
        (dates, day_initial, meal_initial) = self.get_meals(host_eg, guest_eg, 'manage' in self.request.GET)
        dates = self.get_meal_dates(dates, formsets['day_formset'], formsets['meal_formset'])
#        sys.stderr.write("SETTING DATES\n\n" + pformat(dates) + "\n")

        # XXX - at least this gets it into the context...
        formsets['invite_dates'] = dates
        formsets['host_eg'] = host_eg
        formsets['guest_eg'] = guest_eg

        if not self.request.user.is_authenticated():
            if not formsets['user_formset'].is_valid():
                return False
        if not host_eg:
            if not formsets['group_formset'].is_valid():
                return False
            if not formsets['grouphost_formset'].is_valid():
                return False
        if not formsets['day_formset'].is_valid():
            return False
        if not formsets['meal_formset'].is_valid():
            return False

        dd = iter(formsets['day_formset'].cleaned_data)
        md = iter(formsets['meal_formset'].cleaned_data)

        missing = False
        for day in dates:
            needed = False
            for meal in day['meals']:
                data = md.next()
                if data['invited']:
                    needed = True
            data = dd.next()
            if needed and not data['dinner_time']:
                day['form'].errors['dinner_time'] = ['You must specify a dinner time']
                missing = True
        if missing:
            return False

        return True

    def save_changes(self, formsets):
        (host_eg, guest_eg) = self.get_egs()
        if host_eg:
            if not host_eg.group.is_admin(self.request.user):
                raise PermissionDenied
        else:
            host_eg = super(EventHostInviteView, self).save_changes(formsets)

        day_data = formsets['day_formset'].cleaned_data
        meal_data = formsets['meal_formset'].cleaned_data

        dd = iter(day_data)
        md = iter(meal_data)
        
        missing = False;

        (dates, day_initial, meal_initial) = self.get_meals(host_eg, guest_eg, 'manage' in self.request.GET)
        dates = self.get_meal_dates(dates, formsets['day_formset'], formsets['meal_formset'])

        for day in dates:
            needed = False
            for meal in day['meals']:
                data = md.next()
                if data['invited']:
                    needed = True
            data = dd.next()
            if needed and not data['dinner_time']:
                day['form'].errors['dinner_time'] = ['You must specify a dinner time']
                missing = True

        if missing:
            context['error'] = True
            return self.render_to_response(context)

        dd = iter(day_data)
        md = iter(meal_data)

        to_invite = []
        to_confirm = []
        to_rescind = []
        to_change = []

        for day in dates:
            data = dd.next()
            dinner_time = data['dinner_time']
            for m in day['meals']:
                mdata = md.next()
                meal = Meal.objects.get(id = mdata['meal_id'])
                if (meal.state == 'N'):
                    if 'invited' in mdata and mdata['invited']:
                        to_invite.append( (meal, dinner_time) )
                    continue
                elif (meal.state == 'I'):
                    if 'invited' not in mdata or not mdata['invited']:
                        if 'manage' in self.request.GET:
                            to_rescind.append(MealInvite.objects.get(host_eg=host_eg,meal=meal))
                    continue
                elif (meal.state == 'S'):
                    if 'invited' in mdata and mdata['invited']:
                        to_confirm.append(meal.invite)
                        continue
                    else:
                        if 'manage' in self.request.GET:
                            to_rescind.append(meal.invite)
                        continue
                elif (meal.state == 'C'):
                    if 'invited' not in mdata or not mdata['invited']:
                        if 'manage' in self.request.GET:
                            to_rescind.append(meal.invite)
                        continue
                if str(meal.invite.dinner_time) != str(dinner_time):
#                    sys.stderr.write("[%s] != [%s]\n" % (meal.invite.dinner_time, dinner_time) )
                    meal.invite.dinner_time = dinner_time
                    to_change.append(meal.invite)

        host_eg.rescind_invites(to_rescind)
        host_eg.confirm_invites(to_confirm)
        host_eg.send_invites(to_invite)
        host_eg.change_invites(to_change)

        host_eg.showConfirm = False
        
        return host_eg

    def get_egs(self):
        host_eg = None
        if 'host' in self.request.GET:
            host_eg = EventGroup.objects.get(id=self.request.GET['host'])
        else:
            if self.request.user.is_authenticated():
                my_groups = self.request.user.get_profile().admin_groups()
                group_events = list(EventGroup.objects.filter(group__in=my_groups, event=self.object, role='T')) 
                if len(group_events) > 1:
                    raise Exception("you have multiple groups at this event")
                if len(group_events) > 0:
                    host_eg = group_events[0]
        guest_eg = None
        if 'guest' in self.request.GET:
            guest_eg = EventGroup.objects.get(id=self.request.GET['guest'])

        return (host_eg, guest_eg)

    def default_role(self):
        return 'T'

    def get_context_data(self, **kwargs):
        (host_eg, guest_eg) = self.get_egs()

        if host_eg:
            if not host_eg.group.is_admin(self.request.user):
                raise PermissionDenied

        kwargs['host_eg'] = host_eg

        context = super(EventHostInviteView, self).get_context_data(**kwargs)

        (dates, day_initial, meal_initial) = self.get_meals(host_eg, guest_eg, 'manage' in self.request.GET)

        day_factory = formset_factory(EventInviteDayForm, extra=0)
        meal_factory = formset_factory(EventInviteMealForm, extra=0)
        day_formset = day_factory(prefix='days', initial=day_initial)
        meal_formset = meal_factory(prefix='meals', initial=meal_initial)

        dates = self.get_meal_dates(dates, day_formset, meal_formset)

        context['invite_dates'] = dates
        context['day_formset'] = day_formset
        context['meal_formset'] = meal_formset
        context['host_eg'] = host_eg
        context['guest_eg'] = guest_eg
        context['manage'] = 'manage' in self.request.GET
        return context

    def get_meals(self, eg, guest_eg=None, manage=False):
        d = { }
        if guest_eg:
            meals = Meal.objects.filter(event=self.object,eg=guest_eg).order_by('date')
        else:
            meals = Meal.objects.filter(event=self.object).order_by('date')
        d = self.filterMeals(meals, eg, guest_eg, manage, 1)

        if (len(d) < 10):
          d = self.filterMeals(meals, eg, guest_eg, manage, 2)

        if (len(d) < 10):
          d = self.filterMeals(meals, eg, guest_eg, manage, 4)

        day_initial = []
        meal_initial = []

        keys = d.keys()
        keys.sort()

        for date in keys:
            dinner_time = ''
            for meal in d[date]:
                meal_initial.append({ 'meal_id' : meal.id, 'invited' : (meal.state != 'N') })
                if not dinner_time:
                    if meal.invite:
                        dinner_time = meal.invite.dinner_time
                    else:
                        try:    
                            invite = MealInvite.objects.get(host_eg=eg,meal=meal)
                            dinner_time = invite.dinner_time
                        except MealInvite.DoesNotExist:
                            pass
            day_initial.append({ 'date' : date, 'dinner_time' : dinner_time })

        return (d, day_initial, meal_initial)

    def filterMeals(self, meals, eg, guest_eg, manage, maxInvites):
        """
            Filters out meals to be selected
            if guest_eg is given, then only meals with that eg will be included
            if manage == false, and guest_eg == NONE, then this method only returns meals in which the
                meal.eg.invites <= maxInvites
        """
        d = {}
        for meal in meals:
            if meal.state == 'S' or meal.state == 'C':
                if not meal.invite:
  #                    sys.stderr.write("no invite :(\n")
                    continue
            if meal.state == 'N':
                if manage:
                    continue
            else:
                invite = meal.invite
                if meal.state == 'I':
                    try:
                        invite = MealInvite.objects.get(host_eg=eg, meal=meal)
                    except MealInvite.DoesNotExist:
                        invite = None
                if not invite or invite.host_eg != eg:
  #                    sys.stderr.write("not mine\n")
                    if manage:
                        continue

            # This is a temporary solution for limiting the meals screen to only show artists with 1 or less invites.
            if (not manage and not guest_eg and len(meal.eg.invites()) > maxInvites):
                continue
            if meal.date not in d:
                d[meal.date] = []
            d[meal.date].append(meal)
          
        return d

    def get_meal_dates(self, dates, day_formset, meal_formset):
        df = iter(day_formset)
        mf = iter(meal_formset)

        keys = dates.keys()
        keys.sort()
        out = []
        for date in keys:
            meals = []
            for meal in dates[date]:
                meals.append({ 'meal' : meal, 'form' : mf.next() })
            out.append({ 'date' : date, 'form' : df.next(), 'meals' : meals })

        return out
