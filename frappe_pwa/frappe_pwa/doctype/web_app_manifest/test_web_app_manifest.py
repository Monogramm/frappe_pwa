# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

from frappe_pwa.frappe_pwa.doctype.web_app_manifest.web_app_manifest import configure_pwa


class TestWebAppManifest(unittest.TestCase):
    def test_configure_pwa(self):
        configure_pwa()
        ws = frappe.get_doc('Website Settings')
        self.assertIn('''rel="manifest"''', ws.head_html)
