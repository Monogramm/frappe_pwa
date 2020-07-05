# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest


class TestWebAppManifest(unittest.TestCase):
    def setUp(self):
        self.web_manifest = frappe.get_doc('Web App Manifest')

    def test_configure_pwa(self):
        self.web_manifest.configure_pwa()
        ws = frappe.get_doc('Website Settings')
        ws.head_html.remove('<link href="/assets/frappe_pwa/manifest.json" rel="manifest">')
        ws.save()
