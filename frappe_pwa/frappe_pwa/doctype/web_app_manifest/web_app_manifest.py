# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document


class WebAppManifest(Document):

    def on_update(self):
        """clear cache"""
        frappe.clear_cache(user='Guest')

        from frappe.website.render import clear_cache
        clear_cache()
