# Purpose #

This page makes it easy for registered theme camps to find art groups to invite to dinner.  It also serves to show potential theme camp registrants that their help is needed.

# Contents #

This should contain a list of all art groups who have not yet been invited to dinner.

Lower on the page, it might also have a list of art groups who have been invited but haven't yet finished the confirmation process.

Ultimately this page will lead the user to the InviteArtistPage

# Alternate Modes #

## Single Artist ##

As a replacement for InviteArtistPage, a guest= parameter can be specified, with a guest EventGroup id, so that only meals for that guest are shown.

## Manage Invitations ##

As a replacement for ManageInvitationsPage, the manage parameter will cause this page to only show invitations that have already been made.

# Screenshot #

Not implemented yet :(

## Data Format ##
The Artist Data needs to be in this format
ex:
```
  var uninvitedArtists = [{
            name: 'Dairy Eaters',
            desc: 'We Love Cheese',
            date: new Date(2011, 8, 28),
            url: 'http://www.myfirefx.com',
            numPeople: 18,
            features: [
              'No Dairy'
            ]
        },{
            name: 'Dairy Seaters',
            desc: 'We Love Cheese',
            date: new Date(2011, 8, 29),
            url: 'http://www.myfirefx.com',
            numPeople: 24,
            features: [
              'No Meat'
            ]
        },{
            name: 'Dairy Meaters',
            desc: 'We Love Cheese so much that it makes us sick....sick to the stomach and we are all lactose intolerant..oops  My bad did I do that?  Also if we liek adfasidk ladjfie lkajsdfi i asdflkjeij asdlfjij ija fij aldsfj ioje iajs dflkj ilaj alijf ij aisj f',
            date: new Date(2011, 8, 29),
            url: 'http://www.myfirefx.com',
            numPeople: 29,
            features: [
              'Vegan'
            ]
        },{
            name: 'Dairy Beaters',
            desc: 'We Love Cheesies',
            date: new Date(2011, 8, 30),
            url: 'http://www.myfirefx.com',
            numPeople: 5,
            features: [
              'No Meat', 'Blah', 'Vegan'
            ]
        },{
            name: 'Dairy Eaters',
            desc: 'We Blah Cheese',
            date: new Date(2011, 8, 31),
            url: 'http://www.myfirefx.com',
            numPeople: 4,
            features: [
              'No Meat', 'Vegetarian'
            ]
        },{
            name: 'Meat Eaters',
            desc: 'We Love Meat',
            date: new Date(2011, 9, 2),
            url: 'http://www.myfirefx.com',
            numPeople: 3,
            features: [
              'No Meat', 'Cold food only'
            ]
        },{
            name: 'Meater Eaters',
            desc: 'We Love Cheese',
            date: new Date(2011, 8, 2),
            url: 'http://www.myfirefx.com',
            numPeople: 9,
            features: [
              'No Meat', 'We like it burning hot'
            ]
        }];

```