PageSummary UserFlows

# Purpose #

This is where a group registers as a theme camp (ie. meal host) at a particular event.

# Contents #

  * If the user is not authenticated, they will be be passed thru FacebookConnectPage first.
  * If the user declines FB connection, this page will collect basic user information.  See UserRegistrationForm for details.
  * If the user has usable Facebook entities (ie. groups, events, or pages) that can be registered as a theme camp, they will be listed with radio buttons.  See GroupSelectionForm for details.
  * If the user already has a registered group that is not attending this event, it should also be listed with a radio button. ([Issue 20](https://code.google.com/p/nourish/issues/detail?id=20))
  * If the user has no usable FB entities (or declines to use them), this page will collect basic group information.  See GroupRegistrationForm for details.
  * This page will always collect general information about event meals, such as times and locations.  See HostMealForm for details.

# Main Copy #

```

Register a Theme Camp at $event

This page is for theme camps that would like to invite artists to dinner at $event.

```

_Note that copy specifically related to user, group, or meal details should be defined on the GroupSelectionForm, UserRegistrationForm, GroupRegistrationForm, or HostMealForm pages._


# Screenshot #

![http://nourish.googlecode.com/files/ThemeCampRegistrationPage.png](http://nourish.googlecode.com/files/ThemeCampRegistrationPage.png)