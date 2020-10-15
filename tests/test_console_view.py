"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   15/10/2020
=============================================
"""

from unittest import TestCase, mock
from src.console_view.console_view import ConsoleView


class TestConsoleView(TestCase):

    @mock.patch('src.console_view.console_view.ConsoleView.get_input', return_value='y')
    def test_get_input(self, input):
        view = ConsoleView()
        result = view.get_input("")
        self.assertEqual(result, 'y')
