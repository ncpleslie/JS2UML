from src.command_line import CommandLine
from src.controller import Controller
from src.console_view.console_view import ConsoleView
from src.converter.converter_director import ConverterDirector
from src.converter.js_parser_builder import JSParserBuilder
from src.parser_factory.user_defined_parser_creator import UserDefinedParserCreator
from src.converter.converter import Converter

if __name__ == "__main__":
    controller = Controller(
        ConsoleView(), Converter(JSParserBuilder()), UserDefinedParserCreator(ConsoleView()))
    CommandLine(controller).cmdloop()
