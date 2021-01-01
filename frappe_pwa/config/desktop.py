# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    """Returns the application desktop icons configuration."""
    return [
        {
            "module_name": "Frappe PWA",
            "color": "#5A0FC8",
            "icon": "octicon octicon-globe",
            "type": "module",
            "label": _("Frappe PWA")
        }
    ]
