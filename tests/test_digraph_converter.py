"""==========================================
; Title:  Tests for Digraph Converter
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""

from unittest import TestCase
from graphviz import Digraph
from os import path
from js2uml.converter.digraph_converter import DigraphConverter


class TestDigraphConverter(TestCase):

    def test_convert_expected_input(self):
        # arrange
        digraph_parser = DigraphConverter()
        parsed_string = [{'class_name': 'Patient', 'attributes': [
            'issue'], 'methods': ['constructor'], 'edges': {'Object'}}]
        expected_result = Digraph()
        # act
        result = digraph_parser.convert(parsed_string)
        # assert
        self.assertEqual(type(result), type(expected_result))

    def test_convert_unexpected_input(self):
        # arrange
        digraph_parser = DigraphConverter()
        parsed_string = ""
        expected_result = Digraph()
        # act
        result = digraph_parser.convert(parsed_string)
        # assert
        self.assertNotEqual(type(result), type(expected_result))

    def test_render_expected_input(self):
        # arrange
        digraph_parser = DigraphConverter()
        input = Digraph()
        expected_filename = 'test_file'
        expected_file_format = 'png'
        # act
        digraph_parser.render(input, expected_filename, expected_file_format)
        is_there = path.isfile(
            f"{expected_filename}.{expected_file_format}")
        # assert
        self.assertTrue(is_there)

    def test_render_unexpected_input(self):
        # arrange
        digraph_parser = DigraphConverter()
        input = object()
        expected_filename = 'test_file'
        expected_file_format = 'png'
        expected_exception = Exception
        # act
        # assert
        with self.assertRaises(expected_exception):
            digraph_parser.render(
                input, expected_filename, expected_file_format)
