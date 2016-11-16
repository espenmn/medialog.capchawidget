# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from medialog.captchawidget import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider


class IMedialogCaptchawidgetLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRecaptchaSettings(form.Schema):
    """Your google captcha keys
    """

    form.fieldset(
        'captcha',
        label=_(u'Captcha'),
        fields=[
             'key',
             'secret',
            ],
     )

    key = schema.TextLine (
    	title=_(u"label_key", default=u"Site Key"),
    )

    secret = schema.TextLine (
    	title=_(u"label_secret", default=u"Secret Key"),
    )

        
alsoProvides(IRecaptchaSettings, IMedialogControlpanelSettingsProvider)