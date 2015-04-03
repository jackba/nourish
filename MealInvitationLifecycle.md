

# Implementation #

This describes the behind-the-scenes workings, regardless of the UI

There are two types of objects involved in the invitation process, a Meal and a MealInvite.

## Objects ##

### Meal ###

  * State (New, Invited, Selected, Confirmed)
  * Date
  * EventGroup requesting the meal
  * Meal Type ("Dinner")
  * Number of diners
  * Flags (ie. "Food Restrictions")
  * Notes
  * MealInvite reference (if selected or confirmed)

### Invite ###

  * State (New, Selected, Confirmed, Declined)
  * EventGroup hosting the meal
  * Meal reference

## Operations ##

### Artist group registration ###

  * For each day that a crew count is mentioned, a Meal object is created.

### Theme camp invites art group ###

(if the group is invited for multiple days/meals, then the following applies to each day/meal)

  * For each Meal object (possibly several, if they are invited for several days), a Invite object is created with a state of 'New'
  * For each Meal object that is invited, the Meal's state will be set to 'Invited' if it is 'New'.

### Artist group chooses an invitation ###

(if the group chooses invitations for multiple days/meals, then the following applies to each day/meal)

  * The Meal and Invite state are both set to 'Selected'.
  * Any other Meal Invites associated with the Meal have their state set to 'New'.

### Theme camp confirms invitation ###

(if the camp confirms invitations for multiple days/meals, then the following applies to each day/meal)

  * The Meal and Invite state are both set to 'Confirmed'.
  * Any other Invites for the same Meal have their state set to 'Declined'.

### Theme camp deletes invitation ###

(if the camp deletes invitations for multiple days/meals, then the following applies to each day/meal)

  * If any other MealInvites are associated with the Meal, their state is set to 'New' and the Meal's state is set to 'Invited.
  * If no other MealInvites are associated with the Meal, it's state is set to 'New'.