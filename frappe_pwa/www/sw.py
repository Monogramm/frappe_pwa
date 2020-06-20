# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals
import frappe

no_sitemap = 1
base_template_path = "templates/www/sw.js"


def get_context(context):
	hooks = frappe.get_hooks()

	context.web_include_js = hooks.web_include_js or []

	context.web_include_css = hooks.web_include_css or []

	if not context.get("favicon"):
		context["favicon"] = "/assets/frappe/images/favicon.png"

	settings = frappe.get_single("Website Settings")
	if settings.favicon and settings.favicon != "attach_files:":
		context["favicon"] = settings.favicon
