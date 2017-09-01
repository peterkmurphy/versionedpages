from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import VersionPage, VersionPageRevision
from mezzanine.core.admin import StackedDynamicInlineAdmin

class VersionPageRevisionInline(StackedDynamicInlineAdmin):
    model = VersionPageRevision
    extra = 0


class VersionPageAdmin(PageAdmin):
    inlines = (VersionPageRevisionInline,)


admin.site.register(VersionPage, VersionPageAdmin)
