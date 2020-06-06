# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    """Returns the application desktop icons configuration."""
    return [
        {
            "module_name": "ERPNext Template",
            "color": "grey",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("ERPNext Template")
        }
    ]
