"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   16/10/2020
=============================================
"""

from unittest import TestCase, mock
from src.controller import Controller
from src.converter.converter import Converter


class MockConsoleView:
    count = -1

    def show(self, msg):
        print(msg)

    def get_input(self, msg):
        print('I got called')
        self.count += 1
        iter_value = ['test_js/basic', 'filename', 'png']
        return iter_value[self.count]

    def get_yes_no_input(self, msg):
        return 'Y'


class TestCommandLine(TestCase):

    def test_parse_no_args(self):
        controller = Controller(MockConsoleView(), Converter())
        controller.parse(None)
        self.assertTrue
