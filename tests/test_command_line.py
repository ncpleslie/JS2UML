"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   15/10/2020
=============================================
"""

from unittest import TestCase
from src.command_line import CommandLine
from src.controller import Controller
from src.console_view.console_view import ConsoleView
from src.converter.converter_director import ConverterDirector
from src.converter.js_parser_builder import JSParserBuilder


class TestCommandLine(TestCase):
    def test_exit(self):
        cmd_line = CommandLine(Controller(None, None))
        expected_result = SystemExit
        with self.assertRaises(expected_result):
            cmd_line.do_exit(None)

    def test_help_with_args(self):
        cmd_line = CommandLine(Controller(None, None))
        args = "exit"
        cmd_line.do_help(args)
        self.assertTrue

    def test_help_without_args(self):
        cmd_line = CommandLine(Controller(ConsoleView(), None))
        cmd_line.do_help(None)
        self.assertTrue

    def test_setup(self):
        cmd_line = CommandLine(Controller(ConsoleView(), None))
        input = '-f test_js/basic -o filename -t png'
        cmd_line.do_setup(input)
        self.assertTrue

    def test_parse(self):
        cmd_line = CommandLine(Controller(
            ConsoleView(), ConverterDirector(JSParserBuilder())))
        input = '-f test_js/basic -o filename -t png'
        cmd_line.do_parse(input)
        self.assertTrue
