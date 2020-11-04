from src.command_line import CommandLine
from src.controller import Controller
from src.console_view.console_view import ConsoleView
from src.converter.converter_director import ConverterDirector
from src.converter.js_parser_builder import JSParserBuilder


if __name__ == "__main__":
    controller = Controller(
        ConsoleView(), ConverterDirector(JSParserBuilder()))
    CommandLine(controller).cmdloop()
