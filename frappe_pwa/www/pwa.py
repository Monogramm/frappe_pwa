# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import frappe

no_sitemap = 1
base_template_path = "templates/www/pwa.js"


def get_context(context):
    service_worker = frappe.db.get_singles_dict("Service Worker")
    context.vapid_public_key = service_worker.vapid_public_key or ""
