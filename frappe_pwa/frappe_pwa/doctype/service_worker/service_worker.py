# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class ServiceWorker(Document):
	def generate_vapid_key(self, event="vapid_progress_bar"):
		frappe.publish_realtime(event, {"progress": "0"}, user=frappe.session.user)

		# TODO Generate VAPID keys
		# https://github.com/web-push-libs/vapid/tree/main/python
		

		frappe.publish_realtime(
			event, {"progress": [100, 100]}, user=frappe.session.user)

		return False
