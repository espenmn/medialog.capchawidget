# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from medialog.captchawidget.testing import MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING  # noqa
from medialog.captchawidget.interfaces import IKast

import unittest2 as unittest


class KastIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Kast')
        schema = fti.lookupSchema()
        self.assertEqual(IKast, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Kast')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Kast')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IKast.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Kast', 'Kast')
        self.assertTrue(
            IKast.providedBy(self.portal['Kast'])
        )
