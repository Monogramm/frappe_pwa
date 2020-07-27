# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    """Returns the module desktop links configuration."""
    return [
		{
			"label": _("Web App Manifest"),
			"items": [
				{
					"type": "doctype",
					"name": "Web App Manifest",
					"description": _("Web App Manifest"),
				}
				]
		},
		{
			"label": _("Service Worker"),
			"items": [
				{
					"type": "doctype",
					"name": "Service Worker",
					"description": _("Service Worker"),
				}
				]
		}
    ]
