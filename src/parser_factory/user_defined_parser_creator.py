from src.parser_factory.abstract_parser_creator import AbstractParserCreator
from src.converter.model.abstract_parser_builder import AbstractParserBuilder
from src.converter.js_parser_builder import JSParserBuilder
from src.converter.py_parser_builder import PyParserBuilder
from src.console_view.iconsole_view import IConsoleView


class UserDefinedParserCreator(AbstractParserCreator):
    def __init__(self, iconsole_view: IConsoleView):
        self._view = iconsole_view

    def pick_parser_factory(self) -> AbstractParserBuilder:
        response = self._view.get_yes_no_input(
            "Convert JS files? Enter 'Y'.\nConvert Py files? Enter 'n'")

        if response:
            return JSParserBuilder()
        return PyParserBuilder()
