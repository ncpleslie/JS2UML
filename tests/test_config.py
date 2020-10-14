"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""

from unittest import TestCase
from js2uml.io.config import Config


class TestConfig(TestCase):

    def test_get_default_filename(self):
        # arrange
        expected_result = "filename"
        # act
        result = Config.get_default_filename()
        # assert
        self.assertEqual(result, expected_result)

    def test_get_default_filetype(self):
        # arrange
        expected_result = "png"
        # act
        result = Config.get_default_filetype()
        # assert
        self.assertEqual(result, expected_result)

    def test_get_storage_location(self):
        # arrange
        expected_result = "test_js"
        # act
        result = Config.get_default_storage_location()
        # assert
        self.assertEqual(result, expected_result)
