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
from src.parser_factory.user_defined_parser_creator import UserDefinedParserCreator
from src.console_view.iconsole_view import IConsoleView


class MockConsoleView(IConsoleView):
    count = -1

    def __init__(self, output):
        self.output = output

    def show(self, msg):
        print(msg)

    def get_input(self, msg):
        self.count += 1
        iter_value = ['test_js/basic', 'filename', 'png']
        return iter_value[self.count]

    def get_yes_no_input(self, msg):
        return self.output


class TestCommandLine(TestCase):
    def test_exit(self):
        cmd_line = CommandLine(Controller(None, None, None))
        expected_result = SystemExit
        with self.assertRaises(expected_result):
            cmd_line.do_exit(None)

    def test_help_with_args(self):
        cmd_line = CommandLine(Controller(None, None, None))
        args = "exit"
        cmd_line.do_help(args)
        self.assertTrue

    def test_help_without_args(self):
        cmd_line = CommandLine(Controller(ConsoleView(), None, None))
        cmd_line.do_help(None)
        self.assertTrue

    def test_setup(self):
        cmd_line = CommandLine(Controller(ConsoleView(), None, None))
        input = '-f test_js/basic -o filename -t png'
        cmd_line.do_setup(input)
        self.assertTrue

    def test_parse(self):
        cmd_line = CommandLine(Controller(ConsoleView(), ConverterDirector(
            JSParserBuilder()), UserDefinedParserCreator(MockConsoleView(True))))
        input = '-f test_js/basic -o filename -t png'
        cmd_line.do_parse(input)
        self.assertTrue

    def test_change(self):
        cmd_line = CommandLine(Controller(
            ConsoleView(), ConverterDirector(JSParserBuilder()), UserDefinedParserCreator(MockConsoleView(True))))
        cmd_line.do_change(None)
        self.assertTrue

    def test_change_with_false(self):
        cmd_line = CommandLine(Controller(
            ConsoleView(), ConverterDirector(JSParserBuilder()), UserDefinedParserCreator(MockConsoleView(False))))
        cmd_line.do_change(None)
        self.assertTrue
