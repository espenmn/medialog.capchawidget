# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.captchawidget


class MedialogCaptchawidgetLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=medialog.captchawidget)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.captchawidget:default')


MEDIALOG_CAPCHAWIDGET_FIXTURE = MedialogCaptchawidgetLayer()


MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_CAPCHAWIDGET_FIXTURE,),
    name='MedialogCaptchawidgetLayer:IntegrationTesting'
)


MEDIALOG_CAPCHAWIDGET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_CAPCHAWIDGET_FIXTURE,),
    name='MedialogCaptchawidgetLayer:FunctionalTesting'
)


MEDIALOG_CAPCHAWIDGET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_CAPCHAWIDGET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MedialogCaptchawidgetLayer:AcceptanceTesting'
)
