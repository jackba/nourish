

# Introduction #

This page documents various ways a user can experience the ORS.

Some background can be found at MealInvitationLifecycle.

Each section describes one specific common user flow.  Starting with a Site Promotor (ie. FtA communications person) inviting an event organizer to register, all major primary use cases of the application are covered.

For a complete list of pages, see PageSummary.

# Flows #

## Site Promoter ##

  1. You navigate to the page you wish to promote
  1. You click the appropriate promotion button

#### Kinds of Promotions ####

  * Tell a new event organizer (results in a new user enterting [UserFlows#Event\_Lead](UserFlows#Event_Lead.md))
  * Tell anyone about an event (leads to ??)
  * Tell a theme camp about an event (results in a new user entering [UserFlows#Theme\_Camp\_Lead](UserFlows#Theme_Camp_Lead.md))
  * Tell an art group about an event (results in a new user entering [UserFlows#Art\_Group\_Lead](UserFlows#Art_Group_Lead.md))


## Event Lead ##

  1. You receive an invitation in your FB or inbox and click on it
  1. You arrive at the NotificationLandingPage
  1. You click "Register Event" and go to FacebookConnectPage
  1. You arrive at the EventRegistrationPage
  1. You select your event or enter it's info and click register
  1. Registration is complete, you should be encouraged to take followup actions to promote your event.  See [UserFlows#Site\_Promoter](UserFlows#Site_Promoter.md).


## Theme Camp Lead ##

  1. You receive an invitation in your FB or inbox and click on it
  1. You arrive at the NotificationLandingPage
  1. You click "Register Theme Camp" and go to FacebookConnectPage
  1. You arrive at the ThemeCampRegistrationPage
  1. You select your group from the list or enter your group details and click register
  1. Registration is complete, you are taken to [UserFlows#New\_Theme\_Camp](UserFlows#New_Theme_Camp.md).

## Art Group Lead ##

  1. You receive an invitation in your FB or inbox and click on it
  1. You arrive at the NotificationLandingPage
  1. You click "Register Art Group" and are prompted with FacebookConnectPage
  1. You arrive at the ArtistRegistrationPage
  1. You select your group from the list or enter your group details and click register
  1. Registration is complete, you should be encouraged to promote the event to other theme camps and art groups.  See [UserFlows#Site\_Promoter](UserFlows#Site_Promoter.md).

## New Theme Camp ##

  1. You arrive at UninvitedArtistsPage
  1. You select an artist you are interested in inviting
  1. You arrive at the InviteArtistPage
  1. You select the days you wish to invite them and click save (art group will return thru [UserFlows#Artist\_Invited](UserFlows#Artist_Invited.md))
  1. You are returned to UninvitedArtistsPage.

## Artist invited ##

  1. You receive a notification that you've been invited to dinner, and click on it
  1. You arrive at the NotificationLandingPage
  1. You click "Accept Invitation" (theme camp will return thru [UserFlows#Invite\_Accepted](UserFlows#Invite_Accepted.md))
  1. You are returned to your HomePage

## Invite Accepted ##

  1. You receive a notification that one of your invitations has been accepted, and click on it
  1. You arrive at the NotificationLandingPage
  1. You click "Confirm Invitation" (art group will return thru [UserFlows#Invite\_Confirmed](UserFlows#Invite_Confirmed.md))
  1. You are returned to your HomePage

## Invite Confirmed ##

  1. You receive a notification that your invitation to dinner has been confirmed, and click on it
  1. You arrive at the NotificationLandingPage
  1. You click "Delete Notice"
  1. You are returned to your HomePage