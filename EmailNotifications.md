# Introduction #

Site notifications for the ORS are largely a finished feature... See NotificationTypes and NotificationLandingPage for an overview.

Email delivery itself is a pain.  Bounces, unsubscriptions, etc.  Doing it properly is not nearly as simple as simply firing off the email and forgetting it.

Maybe we should just use a managed service.  Do we have the budget to spend $0.02 for every site update we send?  This is certainly a motivation to let users get their updates via a free and fully managed channel (see [FacebookIntegration#Notifications](FacebookIntegration#Notifications.md)).

# How it will work #

Once we get past the problem of actually sending the emails in a responsible and legal manner, the technical implementation is simply a  matter of adding a new delivery mechanism to the backend for NotificationTypes.  All landing pages and followup actions will remain the same.