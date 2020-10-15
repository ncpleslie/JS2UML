"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""

from unittest import TestCase
from src.input_output.config import Config


class TestConfig(TestCase):

    def test_get_default_filename(self):
        # arrange
        expected_result = "filename"
        # act
        result = Config.get_default_filename()
        # assert
        self.assertEqual(result, expected_result)

    def test_set_default_filename(self):
        # arrange
        expected_input = "filename"
        # act
        Config.set_default_filename(expected_input)
        # assert
        self.assertTrue

    def test_set_default_filename_invalid_input(self):
        # arrange
        expected_input = None
        # act
        Config.set_default_filename(expected_input)
        # assert
        self.assertTrue

    def test_get_default_filetype(self):
        # arrange
        expected_result = "png"
        # act
        result = Config.get_default_filetype()
        # assert
        self.assertEqual(result, expected_result)

    def test_set_default_filetype(self):
        # arrange
        expected_result = "png"
        # act
        Config.set_default_filetype(expected_result)
        # assert
        self.assertTrue

    def test_set_default_filetype_invalid_input(self):
        # arrange
        unexpected_input = 'abcabc'
        # act
        expected_error = IOError
        # assert
        with self.assertRaises(expected_error):
            Config.set_default_filetype(unexpected_input)

    def test_get_storage_location(self):
        # arrange
        expected_result = "test_js/basic"
        # act
        result = Config.get_default_storage_location()
        # assert
        self.assertEqual(result, expected_result)

    def test_set_storage_location(self):
        # arrange
        expected_result = "test_js/basic"
        # act
        Config.set_default_storage_location(expected_result)
        # assert
        self.assertTrue

    def test_set_storage_location_invalid_input(self):
        # arrange
        expected_result = None
        # act
        Config.set_default_storage_location(expected_result)
        # assert
        self.assertTrue

    def test___open_invalid_filename(self):
        invalid_filename = ""
        expected_error = FileNotFoundError
        with self.assertRaises(expected_error):
            Config._Config__open(invalid_filename)

    def test___save_invalid_data(self):
        invalid_data = None
        expected_error = AttributeError
        with self.assertRaises(expected_error):
            Config._Config__save(invalid_data)
