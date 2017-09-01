# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mezzanine.core.models import Slugged, TimeStamped, Ownable
from mezzanine.pages.models import Page, RichText
from django.utils.translation import ugettext_lazy as _, ugettext

class VersionPage(Page, RichText):
    """
    For versioned pages.
    """
    class Meta:
        verbose_name = _("Versioned page")
        verbose_name_plural = _("Versioned pages")

class VersionPageRevision(Ownable, TimeStamped):
    """
    A wiki page revision.
    """

    page = models.ForeignKey("VersionPage", verbose_name=_("Versioned page"))
    content = models.TextField(_("Content"))
    description = models.CharField(_("Description"),
                                   max_length=400, blank=True)

    class Meta:
        verbose_name = _("Versioned revision")
        verbose_name_plural = _("Versioned revisions")
        ordering = ("-created",)

    def __unicode__(self):
        return "%s" % self.created
