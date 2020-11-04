from src.parser_factory.abstract_parser_creator import AbstractParserCreator
from src.converter.model.abstract_parser_builder import AbstractParserBuilder
from src.converter.js_parser_builder import JSParserBuilder
from src.converter.py_parser_builder import PyParserBuilder
from src.console_view.iconsole_view import IConsoleView
from random import seed
from random import randint


class RandomParserCreator(AbstractParserCreator):
    def __init__(self, iconsole_view: IConsoleView):
        self._view = iconsole_view
        self.__threshold = 5

    def pick_parser_factory(self) -> AbstractParserBuilder:
        self._view.show(
            "Changing what files can be converted. WILDCARD BABY! YEEHAW!")
        self.__generate_random_number()
        if self.__generate_random_number() <= self.__threshold:
            return JSParserBuilder()
        return PyParserBuilder()

    def __generate_random_number(self):
        seed(1)
        return randint(0, 10)
