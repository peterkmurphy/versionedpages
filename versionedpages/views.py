# Versioned Pages views.py - This is only called when the index page
# is involved.

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.template.response import TemplateResponse

def page(request, template=u"pages/versionpage.html", extra_context=None):
    """
    Select a template for a page and render it. The request
    object should have a ``page`` attribute that's added via
    ``mezzanine.pages.middleware.PageMiddleware``. The page is loaded
    earlier via middleware to perform various other functions.
    The urlpattern that maps to this view is a catch-all pattern, in
    which case the page attribute won't exist, so raise a 404 then.

    For template selection, a list of possible templates is built up
    based on the current page. This list is order from most granular
    match, starting with a custom template for the exact page, then
    adding templates based on the page's parent page, that could be
    used for sections of a site (eg all children of the parent).
    Finally at the broadest level, a template for the page's content
    type (it's model class) is checked for, and then if none of these
    templates match, the default pages/page.html is used.
    """

    from mezzanine.pages.middleware import PageMiddleware
    if not PageMiddleware.installed():
        raise ImproperlyConfigured("mezzanine.pages.middleware.PageMiddleware "
                                   "(or a subclass of it) is missing from " +
                                   "settings.MIDDLEWARE_CLASSES or " +
                                   "settings.MIDDLEWARE")
    return TemplateResponse(request, [template], extra_context or {})
