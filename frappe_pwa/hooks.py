# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for hooks."""

from __future__ import unicode_literals


app_name = "frappe_pwa"
app_title = "Frappe PWA"
app_publisher = "Monogramm"
app_description = "PWA setup for Frappe website."
app_icon = "octicon octicon-globe"
app_color = "#5A0FC8"
app_email = "opensource@monogramm.io"
app_license = "AGPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_pwa/css/frappe_pwa.css"
# app_include_js = "/assets/frappe_pwa/js/frappe_pwa.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_pwa/css/frappe_pwa.css"
web_include_js = [
    "pwa.js",
    "sw.js"
]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_pwa.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_pwa.install.before_install"
# after_install = "frappe_pwa.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_pwa.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_pwa.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_pwa.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_pwa.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_pwa.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_pwa.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_pwa.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_pwa.event.get_events"
# }

