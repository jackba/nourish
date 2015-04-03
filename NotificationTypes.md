

# Introduction #

There are a variety of types of site notifications that can be sent by the system.

See also: NotificationLandingPage

# Delivery Mechanisms #

## Facebook ##

Notifications can be sent in the form of Facebook "apprequests", if the recipient has a linked facebook account.

## Email ##

Email delivery is not implemented yet.  See EmailNotifications.

# Notification Types #

## Site Invitations ##

These notifications are used to encourage new users to visit the site and start using it.  They are sent by other users, and can be represented as private, user-to-user communications.

### Register your Event ###

[Issue 21](https://code.google.com/p/nourish/issues/detail?id=21)

### Register your Theme Camp ###

```

$user thinks you should register your theme camp at $event, so you can
invite artists to dinner!

```

http://code.google.com/p/nourish/source/browse/templates/fb/event_host_siteinvite_link.html
http://code.google.com/p/nourish/source/browse/templates/notif/event_host_siteinvite.html

### Register your Art Group ###

```

$sender thinks you should register your theme camp at $event, so you can
invite artists to dinner!

```

http://code.google.com/p/nourish/source/browse/templates/fb/event_guest_siteinvite_link.html
http://code.google.com/p/nourish/source/browse/templates/notif/event_guest_siteinvite.html

## Site Updates ##

These notifications are used to let existing users know about changes to their meal reservations and other interesting events in the system.  The are sent by the system itself, and should be represented as private, single-user updates.

### Sent to Guests ###

#### You've been invited ####

```

$host invited $guest to dinner at $event!

```

http://code.google.com/p/nourish/source/browse/templates/notif/invited.html
http://code.google.com/p/nourish/source/browse/templates/notif/invited.txt

#### Your invitation has been confirmed ####

```

$host confirmed $guest's invitation to dinner at $event!

```

http://code.google.com/p/nourish/source/browse/templates/notif/confirmed.html
http://code.google.com/p/nourish/source/browse/templates/notif/confirmed.txt

#### Your invitation has been rescinded ####

```

One or more of $guest's confirmed invitations to dinner at $event were cancelled.

```

http://code.google.com/p/nourish/source/browse/templates/notif/rescinded.html
http://code.google.com/p/nourish/source/browse/templates/notif/rescinded.txt

#### Your invitation's dinner time, address or details have changed ####

[Issue 21](https://code.google.com/p/nourish/issues/detail?id=21)

### Sent to Hosts ###

#### Your invitation has been accepted ####

```

$guest accepted $host's invitation(s) to dinner at $event!

```

http://code.google.com/p/nourish/source/browse/templates/notif/chosen.html
http://code.google.com/p/nourish/source/browse/templates/notif/chosen.txt

#### A confirmed invitation has cancelled ####

[Issue 21](https://code.google.com/p/nourish/issues/detail?id=21)

#### A confirmed invitation has updated their headcount or restrictions ####

```

$guest changed details about their confirmed dinners with $host at $event.

```

http://code.google.com/p/nourish/source/browse/templates/notif/changed.html
http://code.google.com/p/nourish/source/browse/templates/notif/changed.txt

#### A confirmed invitation has added another dinner ####

[Issue 21](https://code.google.com/p/nourish/issues/detail?id=21)

#### Playa address is still unset ####

[Issue 21](https://code.google.com/p/nourish/issues/detail?id=21)