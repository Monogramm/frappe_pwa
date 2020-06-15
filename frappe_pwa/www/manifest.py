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

    context.icons = frappe.get_all("Web App Manifest Icon", fields=['*'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})
    if not context.icons:
        context.icons = [{"src": "/assets/frappe/images/favicon.png",
                          "sizes": "128x128", "type": "image/png"}]

    context.categories = frappe.get_all("Web App Manifest Category", fields=['*'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})

    context.screenshots = frappe.get_all("Web App Manifest Screenshot", fields=['*'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})

    context.prefer_related_applications = pwa_manifest.prefer_related_applications
    context.related_applications = frappe.get_all("Web App Manifest Related Application", fields=['*'], filters={
        "parenttype": "Web App Manifest", "parent": pwa_manifest.name})
