from unittest import TestCase
from graphviz import Digraph
from src.converter.digraph_converter import DigraphConverter


class TestConverter(TestCase):

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

    def test_parse_expected_input(self):
        # arrange
        js_parser = JSParser()
        js_string = 'class Patient {constructor(issue) {this.issue = new Object();} }'
        expected_result = [{'class_name': 'Patient', 'attributes': [
            'issue'], 'methods': ['constructor'], 'edges': {'Object'}}]
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertEqual(result, expected_result)

    def test_parse_unexpected_input(self):
        # arrange
        js_parser = JSParser()
        js_string = ''
        expected_result = []
        # act
        result = js_parser.parse(js_string)
        # assert
        self.assertNotEqual(result, expected_result)
