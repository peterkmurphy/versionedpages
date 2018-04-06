from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import VersionPage #, VersionPageRevision
from django.shortcuts import redirect

from reversion_compare.admin import CompareVersionAdmin

class VersionPageAdmin(CompareVersionAdmin):
    pass


# Methods for Django 1.10 and Mezzanine 4.0. Subject to change.

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/admin/pages/page/')

    def response_change(self, request, obj):
        return redirect('/admin/pages/page/')

admin.site.register(VersionPage, VersionPageAdmin)
