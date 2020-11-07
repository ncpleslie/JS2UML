"""==========================================
; Title:  Tests for Converter
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""


from unittest import TestCase
from graphviz import Digraph
from os import path
from src.converter.converter_director import ConverterDirector
from src.errors.digraph_save_exception import DigraphSaveException
from src.converter.js_parser_builder import JSParserBuilder
from src.converter.py_parser_builder import PyParserBuilder


class TestConverter(TestCase):

    def test_save_expected_input(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
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
        converter = ConverterDirector(JSParserBuilder())
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
        converter = ConverterDirector(JSParserBuilder())
        js_string = 'class Patient {constructor(issue) \
            {this.issue = new Object();} }'
        expected_result = Digraph()
        # act
        results = converter.convert(js_string)
        # assert
        self.assertEqual(type(results), type(expected_result))

    def test_convert_unexpected_input(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        incorrect_input = object()
        expected_exception = TypeError

        with self.assertRaises(expected_exception):
            converter.convert(incorrect_input)

    def test_parse_expected_input(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        js_string = 'class Patient {constructor(issue) {this.issue = '\
            'new Object();} aMethod(){console.log(""); const x = new String();}}'
        expected_result = list()
        # act
        result = converter.convert(js_string)
        # assert
        self.assertEqual(type(result.body), type(expected_result))

    def test_parse_partial_expected_input(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        js_string = 'class Patient {constructor(issue) {this.issue = issue} aMethod(){console.log("");}}'
        expected_result = [{'class_name': 'Patient', 'attributes': ['issue'],
                            'methods': ['constructor', 'aMethod'], 'edges': set()}]
        # act
        result = converter.convert(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_partial_new_object_in_expression(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        js_string = 'class Patient {constructor(issue) {this.issue = '\
            'new Object();} aMethod(){console.log(new String());}}'
        expected_result = [{'class_name': 'Patient', 'attributes': [
            'issue'], 'methods': ['constructor', 'aMethod'], 'edges': {'Object', 'String'}}]
        # act
        result = converter.convert(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_empty_class(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        js_string = 'class Patient {}'
        expected_result = list()
        # act
        result = converter.convert(js_string)
        # assert
        self.assertEqual(type(result.body), type(expected_result))

    def test_parse_solo_method(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        js_string = 'class Patient {aMethod(){let y = 1}}'
        expected_result = [{'class_name': 'Patient', 'attributes': [],
                            'methods': ['aMethod'], 'edges': set()}]
        # act
        result = converter.convert(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_unexpected_input(self):
        # arrange
        converter = ConverterDirector(JSParserBuilder())
        js_string = ''
        expected_result = []
        # act
        result = converter.convert(js_string)
        # assert
        self.assertNotEqual(result, expected_result)

    def test_change_builder(self):
        converter = ConverterDirector(JSParserBuilder())

        converter.change_builder(PyParserBuilder())

        self.assertEqual(type(converter.builder), type(PyParserBuilder()))

    def test_py_parse_expected_input(self):
        converter = ConverterDirector(PyParserBuilder())
        valid_input = "class Test:\n\
            def __init__(self):\n\
                self.test = 1\n\
            def aMethod(self):\n\
                self.value = 1"
        expected_output = Digraph()
        result = converter.convert(valid_input)
        self.assertEqual(type(expected_output), type(result))

    def test_py_parse_unexpected_input(self):
        converter = ConverterDirector(PyParserBuilder())
        valid_input = "class Test:\
            def __init__(self):\
                self.test = 1\
            \
            def aMethod(self):\
                self.value = 1"
        expected_output = Digraph()
        result = converter.convert(valid_input)
        self.assertEqual(type(expected_output), type(result))
