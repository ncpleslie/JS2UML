"""==========================================
; Title:  Middleware for JS Parser and Digraph
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from src.converter.abstract_converter import AbstractConverter
from src.converter.js_parser import JSParser
from src.converter.digraph_converter import DigraphConverter
from src.errors.digraph_save_exception import DigraphSaveException


class Converter(AbstractConverter):
    def convert(self, input: str):
        try:
            parsed_js = JSParser().parse(input)
            return DigraphConverter().convert(parsed_js)
        except TypeError as error:
            raise error

    def save(self, dot_graph, filename: str, file_format: str):
        try:
            DigraphConverter().render(dot_graph, filename)
        except Exception as error:
            raise DigraphSaveException("Failed to save digraph")
