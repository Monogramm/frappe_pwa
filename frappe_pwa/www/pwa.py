# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import frappe

no_sitemap = 1
base_template_path = "templates/www/pwa.js"


def get_context(context):
    # TODO Get or generate VAPID for push notifications
    pwa_manifest = frappe.db.get_singles_dict("Web App Manifest")
    context.vapid_public_key = pwa_manifest.vapid_public_key or ""
