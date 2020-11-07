"""==========================================
; Title:  Tests for Config
; Author: Nick Leslie
; Date:   16/10/2020
=============================================
"""

from unittest import TestCase, mock
from os import path, remove
from pickle import dump
from errno import ENOENT
from src.controller import Controller
from src.converter.converter_director import ConverterDirector
from src.console_view.iconsole_view import IConsoleView
from src.input_output.config import Config
from src.converter.js_parser_builder import JSParserBuilder


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

    def test_parse_no_args(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse(None)
        self.assertTrue

    def test_parse_no_args_use_default(self):
        controller = Controller(MockConsoleView(
            False), ConverterDirector(JSParserBuilder()))
        controller.parse(None)
        self.assertTrue

    def test_parse_with_args(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse('-f test_js/basic -o filename -t png')
        self.assertTrue

    def test_parse_remove_config(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse(None)
        self.assertTrue

    def test_parse_remove_config_with_args(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse('-f test_js/basic -o filename -t png')
        self.assertTrue

    def test_parse_remove_config_with_bad_args(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse('abc')
        self.assertTrue

    def test_parse_remove_config_with_filepath_args(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse('-f test_js/ -o filename -t png')
        self.assertTrue

    def test_parse_remove_config_with_bad_filepath_args(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse('-f test/ -o filename -t png')
        self.assertTrue

    def test_parse_remove_config_with_non_js_file(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse(
            '-f test_js/bad/not_a_valid_file.py -o filename -t png')
        self.assertTrue

    def test_parse_remove_config_with_incorrect_filename(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse(
            '-f test_js/bad/incorrect_name.py -o filename -t png')
        self.assertTrue

    def test_parse_remove_config_with_bad_js_file(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.parse(
            '-f test_js/bad/invalid.js -o filename -t png')
        self.assertTrue

    def test_parse_remove_config_replaced_with_bad_config(self):
        filename_config = "config/default_filename"
        filetype_config = "config/default_filetype"
        storage_config = "config/storage_location"

        if path.exists(filename_config):
            remove(filename_config)
        if path.exists(filetype_config):
            remove(filetype_config)
        if path.exists(storage_config):
            remove(storage_config)

        data = {'default_filename': 'not_good'}
        with open(path.join(path.realpath('.'), 'config',
                            list(data.keys())[0]), 'wb') as config:
            dump(data, config)

        data = {'default_filetype': 'not_good'}
        with open(path.join(path.realpath('.'), 'config',
                            list(data.keys())[0]), 'wb') as config:
            dump(data, config)

        data = {'storage_location': 'not_good'}
        with open(path.join(path.realpath('.'), 'config',
                            list(data.keys())[0]), 'wb') as config:
            dump(data, config)

        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))

        controller.parse(
            '-f test_js/bad/invalid.js -o filename -t png')
        self.assertTrue

    def test_setup_with_args(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.setup(
            '-f test_js/bad/invalid.js -o filename -t png')
        self.assertTrue

    def test_setup_without_args(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.setup(None)
        self.assertTrue

    def test_setup_with_bad_args(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller.setup(
            '-f test_js/bad/ -o filename -t abc')
        self.assertTrue

    def test___parse_args_with_no_args(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        controller._Controller__parse_args(None)
        self.assertTrue

    def test___file_reader_error_handler(self):
        controller = Controller(MockConsoleView(
            True), ConverterDirector(JSParserBuilder()))
        error = Exception()
        error.errno = ENOENT
        controller._Controller__file_reader_error_handler(error)
        self.assertTrue
