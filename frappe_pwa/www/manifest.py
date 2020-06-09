# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals
import frappe

no_sitemap = 1
base_template_path = "templates/www/manifest.json"

def get_context(context):
    pwa_manifest = frappe.db.get_singles_dict("Web App Manifest")
    context.app_name = pwa_manifest.app_name or "Frappe Progressive Web Application"

    context.short_name = pwa_manifest.short_name or "Frappe PWA"

    context.theme_color = pwa_manifest.theme_color or "#5e64ff"
    context.background_color = pwa_manifest.background_color or "#FFFFFF"

    context.display = pwa_manifest.display or "fullscreen"
    context.orientation = pwa_manifest.orientation or "any"
    context.dir = pwa_manifest.dir or "auto"
    context.lang = pwa_manifest.lang

    context.scope = pwa_manifest.scope or "/"
    context.start_url = pwa_manifest.start_url or "/"

    # TODO Add icons, screenshots and the other missing fields
    context.icons = [ {"src": "/assets/frappe/images/favicon.png", "sizes": "128x128", "type": "image/png"} ]
    # TODO Default icons to [{"src": "/assets/frappe/images/favicon.png", "sizes": "128x128", "type": "image/png"}]
