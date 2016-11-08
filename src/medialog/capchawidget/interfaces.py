# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from medialog.capchawidget import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider


class IMedialogCapchawidgetLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICapchaSettings(form.Schema):
    """Your google capcha keys
    """

    form.fieldset(
        'capcha',
        label=_(u'Capcha'),
        fields=[
             'key',
             'secret',
            ],
     )

    key = schema.TextLine (
    	title=_(u"label_key", default=u"Key"),
    )

    secret = schema.TextLine (
    	title=_(u"label_secret", default=u"Secret"),
    )

        
alsoProvides(ICapchaSettings, IMedialogControlpanelSettingsProvider)