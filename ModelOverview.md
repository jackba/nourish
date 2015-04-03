

# Primary Objects #

These are the objects that represent things in the application that the end user should easily understand.

## Event ##

This contains all of the information about the event itself.

  * Fields: **name**, **url**, **image\_url**, **description**, **start\_date**, **end\_date**

## Group ##

This is a group, ie. a theme camp or artist group.

  * Fields: **name**, **url**, **image\_url**, **description**

## Meal ##

This is an request for invitation to a single meal on one day.

  * Fields: **date**, **diners**, **features**, **notes**, **state**
  * References: **guest** _(Event Group)_

## Meal Invite ##

This is an invitation from a theme camp to an artist group for a single meal.

  * Fields: **state**
  * References: **Meal**, **host** _(Event Group)_

# Support Objects #

These are objects that track information that is important for the ORS itself, but which may not be directly identifiable by end users.

## Event User ##

This tracks what users are organizing what groups.

  * Fields: **admin**
  * References: **Event**, **User**

## Event Group ##

This tracks what groups are going to what events in what capacity

  * Fields: **event\_address**, **notes**, **role** _(guest/host)_
  * Host-specific Fields: **dinner\_time**, **features**
  * References: **Event**, **Group**

## Group User ##

This tracks what users belong to what groups

  * Fields: **admin**
  * References: **Group**, **User**

## Notification ##

This is a pseudo-object that encapsulates facebook functionality, currently.  The actual data is stored in FB.