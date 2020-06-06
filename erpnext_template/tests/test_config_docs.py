# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt

import unittest

from erpnext_template.config.docs import source_link, docs_base_url, headline, sub_heading, get_context


class TestDocs(unittest.TestCase):
    def test_docs(self):
        self.assertIsNotNone(source_link)
        self.assertIsNotNone(docs_base_url)
        self.assertIsNotNone(headline)
        self.assertIsNotNone(sub_heading)

    def test_get_context(self):
        context = type('obj', (object,), {'brand_html': None,
                                          'source_link': None,
                                          'docs_base_url': None,
                                          'headline': None,
                                          'sub_heading': None})

        get_context(context)

        self.assertIsNotNone(context)

        self.assertIsNotNone(context.brand_html)

        self.assertIsNotNone(context.source_link)
        self.assertEqual(context.source_link, source_link)

        self.assertIsNotNone(context.docs_base_url)
        self.assertEqual(context.docs_base_url, docs_base_url)

        self.assertIsNotNone(context.headline)
        self.assertEqual(context.headline, headline)

        self.assertIsNotNone(context.sub_heading)
        self.assertEqual(context.sub_heading, sub_heading)
