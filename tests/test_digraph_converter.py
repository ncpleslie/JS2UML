"""==========================================
; Title:  Tests for Digraph Converter
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""

from unittest import TestCase
from graphviz import Digraph
from os import path
from src.converter.digraph_converter import DigraphConverter


class TestDigraphConverter(TestCase):

    # def test_convert_expected_input(self):
    #     # arrange
    #     digraph_parser = DigraphConverter()
    #     parsed_string = [{'class_name': 'Patient', 'attributes': [
    #         'issue'], 'methods': ['constructor'], 'edges': {'Object'}}]
    #     expected_result = Digraph()
    #     # act
    #     result = digraph_parser.convert(parsed_string)
    #     # assert
    #     self.assertEqual(type(result), type(expected_result))

    def test_convert_unexpected_input(self):
        # arrange
        digraph_parser = DigraphConverter()
        parsed_string = ""
        expected_result = Digraph()
        # act
        result = digraph_parser.convert(parsed_string)
        # assert
        self.assertNotEqual(type(result), type(expected_result))

    def test_render_all_expected(self):
        # arrange
        digraph_parser = DigraphConverter()
        digraph = Digraph()
        expected_filename = 'test_file'
        expected_file_format = 'png'
        # act
        digraph_parser.render(digraph, expected_filename, expected_file_format)
        is_there = path.isfile(
            f"{expected_filename}.{expected_file_format}")
        # assert
        self.assertTrue(is_there)

    def test_render_unexpected_digraph(self):
        # arrange
        digraph_parser = DigraphConverter()
        digraph = object()
        expected_filename = 'test_file'
        expected_file_format = 'png'
        expected_exception = Exception
        # act
        # assert
        with self.assertRaises(expected_exception):
            digraph_parser.render(
                digraph, expected_filename, expected_file_format)

    def test_render_none_digraph(self):
        # arrange
        digraph_parser = DigraphConverter()
        digraph = None
        expected_filename = 'test_file'
        expected_file_format = 'png'
        expected_exception = Exception
        # act
        # assert
        with self.assertRaises(expected_exception):
            digraph_parser.render(
                digraph, expected_filename, expected_file_format)

    def test_render_unexpected_file_format(self):
        # arrange
        digraph_parser = DigraphConverter()
        digraph = object()
        expected_filename = 'test_file'
        expected_file_format = 'asdasd'
        expected_exception = Exception
        # act
        # assert
        with self.assertRaises(expected_exception):
            digraph_parser.render(
                digraph, expected_filename, expected_file_format)
