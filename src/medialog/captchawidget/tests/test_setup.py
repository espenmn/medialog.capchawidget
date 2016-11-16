# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from medialog.captchawidget.testing import MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.captchawidget is properly installed."""

    layer = MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.captchawidget is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.captchawidget'))

    def test_browserlayer(self):
        """Test that IMedialogCaptchawidgetLayer is registered."""
        from medialog.captchawidget.interfaces import (
            IMedialogCaptchawidgetLayer)
        from plone.browserlayer import utils
        self.assertIn(IMedialogCaptchawidgetLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_CAPCHAWIDGET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.captchawidget'])

    def test_product_uninstalled(self):
        """Test if medialog.captchawidget is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.captchawidget'))

    def test_browserlayer_removed(self):
        """Test that IMedialogCaptchawidgetLayer is removed."""
        from medialog.captchawidget.interfaces import IMedialogCaptchawidgetLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogCaptchawidgetLayer, utils.registered_layers())
