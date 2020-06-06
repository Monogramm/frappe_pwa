# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import unittest

from erpnext_template.hooks import app_title, app_publisher, app_name, app_description, app_icon, app_color, app_email, \
    app_license


class TestDesktop(unittest.TestCase):
    def test_hooks(self):
        self.assertIsNotNone(app_name)
        self.assertIsNotNone(app_title)
        self.assertIsNotNone(app_publisher)
        self.assertIsNotNone(app_description)
        self.assertIsNotNone(app_icon)
        self.assertIsNotNone(app_color)
        self.assertIsNotNone(app_email)
        self.assertIsNotNone(app_license)
