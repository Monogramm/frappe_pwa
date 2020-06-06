# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for docs."""

from __future__ import unicode_literals


source_link = "https://github.com/Monogramm/frappe_pwa"
docs_base_url = "https://monogramm.github.io/frappe_pwa"
headline = "PWA setup for Frappe website."
sub_heading = "Setup website Progressive Web Application."


def get_context(context):
    """Returns the application documentation context.

     :param context: application documentation context"""
    context.brand_html = "Frappe PWA"
    context.source_link = source_link
    context.docs_base_url = docs_base_url
    context.headline = headline
    context.sub_heading = sub_heading
