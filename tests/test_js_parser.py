from unittest import TestCase
from src.converter.js_parser import JSParser


class TestJSParser(TestCase):

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
