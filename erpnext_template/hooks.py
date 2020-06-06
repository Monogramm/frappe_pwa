# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for hooks."""

from __future__ import unicode_literals


app_name = "erpnext_template"
app_title = "ERPNext Template"
app_publisher = "Monogramm"
app_description = "TODO_APP_DESCRIPTION"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "opensource@monogramm.io"
app_license = "AGPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_template/css/erpnext_template.css"
# app_include_js = "/assets/erpnext_template/js/erpnext_template.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_template/css/erpnext_template.css"
# web_include_js = "/assets/erpnext_template/js/erpnext_template.js"

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
# get_website_user_home_page = "erpnext_template.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_template.install.before_install"
# after_install = "erpnext_template.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_template.notifications.get_notification_config"

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
# 		"erpnext_template.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_template.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_template.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_template.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_template.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_template.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_template.event.get_events"
# }

