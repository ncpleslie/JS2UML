"""==========================================
; Title:  Tests for Read
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""

from unittest import TestCase
from src.input_output.read import Read


class TestRead(TestCase):

    def test_load_file_valid_js_file(self):
        # arrange
        read = Read()
        filename = "test_js/basic/basic.js"
        expect_result = "class Patient {\n"\
            "     constructor(issue) {\n"\
            "         this.issue = new Object();\n"\
            "     }\n \n"\
            "     tellSymptons() {\n"\
            "         return this.issue;\n"\
            "     }\n \n"\
            "     feelBetter() {\n"\
            "         this.issue = new Object();\n"\
            "     }\n"\
            " }"
        # act
        results = read.load_file(filename)
        # assert
        self.assertEqual(results, expect_result)

    def test_load_file_valid_js_dir(self):
        # arrange
        read = Read()
        file_dir = "test_js/basic/"
        expect_result = "class Patient {\n"\
            "     constructor(issue) {\n"\
            "         this.issue = new Object();\n"\
            "     }\n \n"\
            "     tellSymptons() {\n"\
            "         return this.issue;\n"\
            "     }\n \n"\
            "     feelBetter() {\n"\
            "         this.issue = new Object();\n"\
            "     }\n"\
            " }"
        # act
        results = read.load_file(file_dir)
        # assert
        self.assertEqual(results, expect_result)

    def test_load_file_invalid_js_file(self):
        # arrange
        read = Read()
        filename = "test_js/basic2.js"
        expected_exception = FileNotFoundError
        # act
        # assert
        with self.assertRaises(expected_exception):
            read.load_file(filename)

    def test_load_file_invalid_js_dir(self):
        # arrange
        read = Read()
        file_dir = "test_js/basic2/"
        expected_exception = FileNotFoundError
        # act
        # assert
        with self.assertRaises(expected_exception):
            read.load_file(file_dir)

    def test__read_file_invalid_filename(self):
        invalid_filename = "abcabc"
        read = Read()
        expected_exception = IOError
        with self.assertRaises(expected_exception):
            read._Read__read_file(invalid_filename)
