"""==========================================
; Title:  Tests for Converter
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""


from unittest import TestCase
from graphviz import Digraph
from os import path
from src.converter.converter import Converter
from src.errors.digraph_save_exception import DigraphSaveException
from src.converter.js_parser import JSParser


class TestConverter(TestCase):

    def test_save_expected_input(self):
        # arrange
        converter = Converter(JSParser())
        input = Digraph()
        expected_filename = 'test_file'
        expected_file_format = 'png'
        # act
        converter.save(input, expected_filename, expected_file_format)
        is_there = path.isfile(
            f"{expected_filename}.{expected_file_format}")
        # assert
        self.assertTrue(is_there)

    def test_save_unexpected_input(self):
        # arrange
        converter = Converter(JSParser())
        input = object()
        expected_filename = 'test_file'
        expected_file_format = 'png'
        expected_exception = DigraphSaveException
        # act
        # assert
        with self.assertRaises(expected_exception):
            converter.save(input, expected_filename, expected_file_format)

    def test_convert_expected_input(self):
        # arrange
        converter = Converter(JSParser())
        js_string = 'class Patient {constructor(issue) \
            {this.issue = new Object();} }'
        expected_result = Digraph()
        # act
        results = converter.convert(js_string)
        # assert
        self.assertEqual(type(results), type(expected_result))

    def test_convert_unexpected_input(self):
        # arrange
        converter = Converter(JSParser())
        incorrect_input = object()
        expected_exception = TypeError

        with self.assertRaises(expected_exception):
            converter.convert(incorrect_input)
