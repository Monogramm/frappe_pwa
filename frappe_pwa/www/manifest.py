# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import json
import frappe

no_sitemap = 1
base_template_path = "templates/www/manifest.json"


def get_context(context):
    pwa_manifest = frappe.db.get_singles_dict("Web App Manifest")
    context.app_name = pwa_manifest.app_name or "Frappe Progressive Web Application"
    context.short_name = pwa_manifest.short_name
    context.theme_color = pwa_manifest.theme_color
    context.background_color = pwa_manifest.background_color
    context.scope = pwa_manifest.scope
    context.start_url = pwa_manifest.start_url
    context.iarc_rating_id = pwa_manifest.iarc_rating_id

    context.description = pwa_manifest.description

    context.display = pwa_manifest.display
    context.orientation = pwa_manifest.orientation

    context.dir = pwa_manifest.dir
    context.lang = pwa_manifest.lang

    context.icons = frappe.get_all("Web App Manifest Icon", fields=['src', 'sizes', 'type'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})
    if not context.icons:
        context.icons = [{"src": "/assets/frappe/images/favicon.png",
                          "sizes": "128x128", "type": "image/png"}
                         ]
    else:
        # Remove optional fields at None
        for i in context.icons:
            if i.sizes is None:
                i.pop("sizes")
            if i.type is None:
                i.pop("type")

    context.icons = json.dumps(context.icons)

    categories = frappe.get_all("Web App Manifest Category", fields=['name'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})
    if categories:
        context.categories = []
        for c in categories:
            context.categories.append(c.name)

        context.categories = json.dumps(context.categories)

    screenshots = frappe.get_all("Web App Manifest Screenshot", fields=['src', 'sizes', 'type'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})
    if screenshots:
        # Remove optional fields at None
        for s in screenshots:
            if s.sizes is None:
                s.pop("sizes")
            if s.type is None:
                s.pop("type")

        context.screenshots = json.dumps(screenshots)

    if pwa_manifest.prefer_related_applications == '0':
        context.prefer_related_applications = 'false'
    elif pwa_manifest.prefer_related_applications == '1':
        context.prefer_related_applications = 'true'
    related_applications = frappe.get_all("Web App Manifest Related Application", fields=['platform', 'url', 'id'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})
    if related_applications:
        # Remove optional fields at None
        for r in related_applications:
            if r.id is None:
                r.pop("id")

        context.related_applications = json.dumps(related_applications)
