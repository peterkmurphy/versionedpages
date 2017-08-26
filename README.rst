========
Overview
========

This application is designed for `Mezzanine
<http://mezzanine.jupo.org/>`_, a content management platform based on the
`Django <https://www.djangoproject.com/>`_ framework. The aim is to allow
admins to edit and store multiple versions of the same rich text page. It
also allows admins to view the differences between different versions.

This application is a fork of `mezzanine-wiki
<https://github.com/dfalk/mezzanine-wiki`>_, which was created by `Dmitry Falk
<mailto:dfalk5@gmail.com>`_. However, there are differences in the goals of
both applications:

1. This application aims to permit different versions of the same Rich Text
   page. The *mezzanine_wiki* app has created its own Page type.
2. This application allows pages to be stored in standard HTML and markdown.
   The *mezzanine_wiki* app supports markdown by default.
3. The *mezzanine_wiki* app allows users to create and edit pages outside of
   the admin; by default, the *versionedpages* application only allows pages to
   be changed in the *Mezzanine* admin.
4. The *versionedpages* application allows pages to be placed anywhere in the
   menu hierarchy of a site. In contrast, the *mezzanine_wiki* app assumes that
   all wiki pages will be located in one directory path in a site.

Requirements
============

The requirements are:

* mezzanine >= 4.0
* diff-match-patch

Quick start
===========

1. Download or clone and run:

    python setup.py install

2. Add "versionedpages" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'versionedpages',
    )

3. Run the following code to create the models:

    python manage.py makemigrations versionedpages
    python manage.py migrate

4. Add "versionedpages.VersionPage" to SEARCH_MODEL_CHOICES setting like this:

    SEARCH_MODEL_CHOICES = ('pages.Page', 'blog.BlogPost', 'versionedpages.VersionPage')

5. Restart the server.

From then on, you should be able to add new pages to the Mezzanine admin. Look
for page types of the form "Versioned Page". From the admin menu, you should also
be able to edit new copies of a page while preserving old ones. You can even
compare different versions of a page. Have fun.
