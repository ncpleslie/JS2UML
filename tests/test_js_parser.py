"""==========================================
; Title:  Tests for JS Parser
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""

from unittest import TestCase
from src.converter.js_parser_builder import JSParserBuilder
from src.converter.extraction import Extraction


class TestJSParser(TestCase):

    def test_parse_expected_input(self):
        # arrange
        js_parser = JSParserBuilder()
        js_string = 'class Patient {constructor(issue) {this.issue = '\
            'new Object();} aMethod(){console.log(""); const x = new String();}}'
        expected_result = list()
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertEqual(type(result.body), type(expected_result))

    def test_parse_partial_expected_input(self):
        # arrange
        js_parser = JSParserBuilder()
        js_string = 'class Patient {constructor(issue) {this.issue = issue} aMethod(){console.log("");}}'
        expected_result = [{'class_name': 'Patient', 'attributes': ['issue'],
                            'methods': ['constructor', 'aMethod'], 'edges': set()}]
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_partial_new_object_in_expression(self):
        # arrange
        js_parser = JSParserBuilder()
        js_string = 'class Patient {constructor(issue) {this.issue = '\
            'new Object();} aMethod(){console.log(new String());}}'
        expected_result = [{'class_name': 'Patient', 'attributes': [
            'issue'], 'methods': ['constructor', 'aMethod'], 'edges': {'Object', 'String'}}]
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_empty_class(self):
        # arrange
        js_parser = JSParserBuilder()
        js_string = 'class Patient {}'
        expected_result = list()
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertEqual(type(result.body), type(expected_result))

    def test_parse_solo_method(self):
        # arrange
        js_parser = JSParserBuilder()
        js_string = 'class Patient {aMethod(){let y = 1}}'
        expected_result = [{'class_name': 'Patient', 'attributes': [],
                            'methods': ['aMethod'], 'edges': set()}]
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_unexpected_input(self):
        # arrange
        js_parser = JSParserBuilder()
        js_string = ''
        expected_result = []
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertNotEqual(result, expected_result)
