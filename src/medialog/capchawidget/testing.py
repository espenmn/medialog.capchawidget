# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.capchawidget


class MedialogCapchawidgetLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=medialog.capchawidget)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.capchawidget:default')


MEDIALOG_CAPCHAWIDGET_FIXTURE = MedialogCapchawidgetLayer()


MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_CAPCHAWIDGET_FIXTURE,),
    name='MedialogCapchawidgetLayer:IntegrationTesting'
)


MEDIALOG_CAPCHAWIDGET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_CAPCHAWIDGET_FIXTURE,),
    name='MedialogCapchawidgetLayer:FunctionalTesting'
)


MEDIALOG_CAPCHAWIDGET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_CAPCHAWIDGET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MedialogCapchawidgetLayer:AcceptanceTesting'
)
