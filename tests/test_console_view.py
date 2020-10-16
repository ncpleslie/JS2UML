"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   15/10/2020
=============================================
"""

from unittest import TestCase, mock
from src.console_view.console_view import ConsoleView


class TestConsoleView(TestCase):

    def test_get_input(self):
        user_input = 'y'
        with mock.patch('builtins.input', return_value=user_input):
            view = ConsoleView()
            result = view.get_input("")
            self.assertEqual(result, user_input)

    def test_get_yes_no_input_valid_input_return_true(self):
        with mock.patch('builtins.input', return_value='y'):
            view = ConsoleView()
            result = view.get_yes_no_input("Test")
            self.assertEqual(result, True)

    def test_get_yes_no_input_valid_input_return_false(self):
        with mock.patch('builtins.input', return_value='n'):
            view = ConsoleView()
            result = view.get_yes_no_input("Test")
            self.assertEqual(result, False)

    def test_get_yes_no_input_no_input(self):
        with mock.patch('builtins.input', return_value='y'):
            view = ConsoleView()
            result = view.get_yes_no_input()
            self.assertEqual(result, True)

    def test_get_yes_no_input_invalid_input(self):
        with mock.patch('builtins.input', return_value='asd'):
            view = ConsoleView()
            result = view.get_yes_no_input()
            self.assertEqual(result, None)
