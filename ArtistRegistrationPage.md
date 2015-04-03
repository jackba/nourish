PageSummary UserFlows

# Purpose #

This is where a group registers as an art project at a particular event.

# Contents #

  * If the user is not authenticated, they will be be passed thru FacebookConnectPage first.
  * If the user declines FB connection, this page will collect basic user information.  See UserRegistrationForm for details.
  * If the user has usable Facebook entities (ie. groups, events, or pages) that can be registered as an art group, they will be listed with radio buttons.  See GroupSelectionForm for details.
  * If the user already has a registered group that is not attending this event, it should also be listed with a radio button. ([Issue 20](https://code.google.com/p/nourish/issues/detail?id=20))
  * If the user has no usable FB entities (or declines to use them), this page will collect basic group information.  See GroupRegistrationForm for details.
  * This page will always collect per-meal information about headcount and restrictions.  See GuestMealForm for details.

# Main Copy #

```

This page is for artist groups that would like to be invited to dinner at $event.

```

_Note that copy specifically related to user, group, or meal details should be defined on the UserRegistrationForm, GroupRegistrationForm, or GuestMealForm pages._

# Template #

http://code.google.com/p/nourish/source/browse/templates/register_event_guest.html

# Screenshot #

![http://nourish.googlecode.com/files/ArtistRegistrationPage.png](http://nourish.googlecode.com/files/ArtistRegistrationPage.png)