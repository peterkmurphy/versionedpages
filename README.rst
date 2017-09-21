========
Overview
========

This application is designed for `Mezzanine
<http://mezzanine.jupo.org/>`_, a content management platform based on the
`Django <https://www.djangoproject.com/>`_ framework. The aim is to allow
admins to edit and store multiple versions of the same rich text page. It
also allows admins to view the differences between different versions.

(September, 2017: this is now more a proof of concept rather than a stand-alone
application - all the legwork is done elsewhere.)

Requirements
============

The requirements are:

* mezzanine >= 4.0
* django-reversion
* django-reversion-compare
* diff-match-patch


Quick start
===========

1. Download or clone and run:

```
    python setup.py install
```

2. Add "versionedpages" to your INSTALLED_APPS setting like this:

```
    INSTALLED_APPS = (
        ...
        'reversion', # https://github.com/etianen/django-reversion
        'reversion_compare', # https://github.com/jedie/django-reversion-compare
        "versionedpages",
    )
```

3. Add reversion models to admin interface:

```
    ADD_REVERSION_ADMIN=True
```

4. Add "versionedpages.VersionPage" to SEARCH_MODEL_CHOICES setting like this:

```
    SEARCH_MODEL_CHOICES = ('pages.Page', 'blog.BlogPost', 'versionedpages.VersionPage')
```

5. Run the following code to create and register the models:

```
    python manage.py makemigrations django-reversion
    python manage.py makemigrations versionedpages
    python manage.py migrate
    python manage.py createinitialrevisions versionedpages.VersionPage
```

6. Restart the server.

From then on, you should be able to add new pages to the Mezzanine admin. Look
for page types of the form "Versioned Page". When editing a page, you can see
the History button. This shows the diffs for different versions of a page.
Have fun.

TBD
===

The first thing to do is better documentation.

The second thing to do is sort out the redirect when the user presses the "Save"
button. At the moment, it goes to a list of pages - like the default Django
admin. What I want is a nicer Mezzanine page. It will work itself out.


Note
====

This application was intended to be a fork of `mezzanine-wiki
<https://github.com/dfalk/mezzanine-wiki>`_, which was created by `Dmitry Falk
<mailto:dfalk5@gmail.com>`_. There were differences in the goals of
both applications:

1. This application allows pages to be stored in standard HTML and markdown.
   The *mezzanine_wiki* app supports markdown by default.
2. The *mezzanine_wiki* app allows users to create and edit pages outside of
   the admin; by default, the *versionedpages* application only allows pages to
   be changed in the *Mezzanine* admin.
3. The *versionedpages* application allows pages to be placed anywhere in the
   menu hierarchy of a site. In contrast, the *mezzanine_wiki* app assumes that
   all wiki pages will be located in one directory path in a site.

The author found that modifying the mezzanine_wiki library to suit his purposes
would be a long and laborious process. In practice, it was easier to use the
django-reversion and django-reversion-compare libraries for the same ends.
