

# Introduction #

The application integrates with Facebook in four distinct ways, not all of which imply the use of each other.

It is important to note that from the very beginning, this application has been designed to function in a freestanding manner with no Facebook use at all.  The Facebook integration just creates a more compelling application for users who are already comfortable with Facebook.

# Advantages of using Facebook integration #

  * Users don't have to remember another password.
  * Users often have a lot less to type when they register, as they can click and choose from existing lists of groups and events.
  * The application doesn't immediately have to handle image uploads and email infrastructure.
  * There are many opportunities for viral propogation of the application thru a community that is heavily Facebook-aware.

# Integration Points #

## Authentication ##

This is the most basic integration.  Using this allows users to avoid having to remember a new username or password.  They can simply click the "Connect with Facebook" button when they return to login to the site, and Facebook will prompt them for their credentials if necessary.

See FacebookConnectPage and LoginPage.

## Graph Objects ##

Various objects related to the user that are accessible via the social graph can be used to populate information about the following objects in this application:

  * The user (useful for single artists, and projects with facebook pages)
  * Groups
  * Pages
  * Events

See FacebookConnectPage, EventSelectionForm, and GroupSelectionForm.

## Notifications ##

Rather than using EmailNotifications, we can send updates via the Facebook "apprequest" notification mechanism. This will let them know about necessary ORS actions on their Facebook homepage.

See NotificationLandingPage.

## Canvas Application ##

The application can run inside of a canvas iframe, which allows it to appear to be part of Facebook.  This lets users interact with all aspects of the application without leaving their Facebook environment.

Most templates in the application do not care if they are displayed in a canvas or a normal freestanding site.  They only thing that changes are the page decorations (ie. the sidebar, header, and footer), and a few minor aspects of user registration and authentication.

See FacebookCanvas.