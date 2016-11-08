# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from medialog.capchawidget.testing import MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.capchawidget is properly installed."""

    layer = MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.capchawidget is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.capchawidget'))

    def test_browserlayer(self):
        """Test that IMedialogCapchawidgetLayer is registered."""
        from medialog.capchawidget.interfaces import (
            IMedialogCapchawidgetLayer)
        from plone.browserlayer import utils
        self.assertIn(IMedialogCapchawidgetLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.capchawidget'])

    def test_product_uninstalled(self):
        """Test if medialog.capchawidget is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.capchawidget'))

    def test_browserlayer_removed(self):
        """Test that IMedialogCapchawidgetLayer is removed."""
        from medialog.capchawidget.interfaces import IMedialogCapchawidgetLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogCapchawidgetLayer, utils.registered_layers())
