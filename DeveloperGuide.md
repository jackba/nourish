

# Introduction #

The FtA website is built using [django](http://www.djangoproject.com/).

We have chosen a fork of django known as [django-nonrel](http://www.allbuttonspressed.com/projects/django-nonrel) because it is friendly towards NoSQL environments, such as those provided by cloud hosting providers (ie. [Google AppEngine](http://code.google.com/appengine/)).

The following "applications" are in use on the site:

  * nourish itself
  * django-socialregistration
  * django-permission-backend-nonrel
  * djangotoolbox
  * dbindexer

Additional underlying libraries include

  * Facebook python SDK
  * python-openid and python-oauth
  * httplib2
  * pyiso8601

# Setting up a dev instance #

## Download tools to get code ##

First you need to have Python installed.  If your on MacOSx, I suggest you download [macports](http://www.macports.org/) and use it to install python and the rest of the tools.

Using macPorts, you can then just
```
sudo port install python
```


you will then need to install mercurial (hg), and git
```
sudo port install mercurial
sudo port install git
sudo port install subversion # is this the right pkg name?
```

## Download runtime tools ##

  * [Sass.](http://sass-lang.com/download.html)
  * [compass](http://compass-style.org/install/)

These will need to be in your PATH when you start manage.py below.

## Create Project Base ##

We're going to create a subdirectory for your dev instance, and everything related to the instance will live under that directory.

This should probably be in your home directory.

```

mkdir fta
cd fta

```

## Check out the code ##

```

mkdir code
cd code
hg clone https://bitbucket.org/wkornewald/django-nonrel
hg clone https://bitbucket.org/wkornewald/django-dbindexer
git clone https://github.com/marcusschwartz/django-socialregistration.git
hg clone https://bitbucket.org/wkornewald/djangotoolbox
git clone git://github.com/kcbanner/facebook-test-users.git
hg clone https://httplib2.googlecode.com/hg/ httplib2
hg clone https://nourish.googlecode.com/hg/ nourish
git clone https://github.com/simplegeo/python-oauth2.git
git clone https://github.com/openid/python-openid.git
git clone https://github.com/facebook/python-sdk.git facebook-python
svn checkout http://pyiso8601.googlecode.com/svn/trunk/ pyiso8601-read-only
#hg clone https://bitbucket.org/fhahn/django-permission-backend-nonrel
hg clone https://bitbucket.org/wkornewald/allbuttonspressed
hg clone https://bitbucket.org/wkornewald/django-mediagenerator
hg clone https://bitbucket.org/twanschik/django-autoload
cd ..


```

## Create the symlinks ##

```

mkdir root
cd root
ln -s ../code/django-nonrel/django .
ln -s ../code/django-dbindexer/dbindexer .
ln -s ../code/djangotoolbox/djangotoolbox .
ln -s ../code/django-socialregistration/socialregistration .
ln -s ../code/facebook-python/src/facebook.py .
ln -s ../code/httplib2/python2/httplib2 .
ln -s ../code/python-oauth2/oauth2 .
ln -s ../code/python-openid/openid .
ln -s ../code/nourish/nourish .
ln -s ../code/nourish/ftasite .
ln -s ../code/nourish/fbcanvas .
ln -s ../code/pyiso8601-read-only/iso8601 .
#ln -s ../code/django-permission-backend-nonrel/permission_backend_nonrel .
ln -s ../code/allbuttonspressed .
ln -s ../code/django-mediagenerator/mediagenerator .
ln -s ../code/django-autoload/autoload .
cd ..

```

## Create localsettings.py ##

This goes in your project base directory.

```

import os

DEBUG = True

SECRET_KEY = 'CHANGE_ME_TO_SOMETHING_LONG_AND_RANDOM'

FACEBOOK_APP_ID = ''
FACEBOOK_API_KEY = ''
FACEBOOK_SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/CHANGE/ME/fta/db.sqlite3',
    }
}

MEDIA_ROOT = '/home/.../media'
STATIC_ROOT = '/home/.../static/'

LOCALPATH = os.path.dirname(__file__)

```

## Populate your database ##

```

python ftasite/manage.py syncdb

```


## Start the dev server ##

```

python ftasite/manage.py runserver

```

## Navigate to your admin page ##

Login with the credentials you created in the syncdb step.

http://127.0.0.1:8000/admin/

## Add an admin UserProfile ##

This is kind of a hack for the moment... you have to manually add a UserProfile record for the admin user, by clicking the "Save" button at the bottom right of the following page:

http://127.0.0.1:8000/admin/nourish/userprofile/add/?fullname=Admin&user=1

You can change the display name if you like, it doesn't matter much...

## Logout and get started ##

First visit http://127.0.0.1:8000/logout/ and then get started at http://127.0.0.1:8000/nourish/.