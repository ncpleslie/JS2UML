"""==========================================
; Title:  Middleware for JS Parser and Digraph
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""
from graphviz import Digraph
from src.converter.model.abstract_converter import AbstractConverter
from src.converter.js_parser import JSParser
from src.converter.digraph_converter import DigraphConverter
from src.errors.digraph_save_exception import DigraphSaveException
from src.converter.model.abstract_parser import AbstractParser
from src.errors.js_parse_exception import JSParseException


class Converter(AbstractConverter):
    """Facilitates the conversion of JS files to UML class diagrams
    """

    def __init__(self, parser: AbstractParser):
        self.parser = parser

    def convert(self, file_data: str) -> Digraph:
        """Converts a JS file to a DOT graph

        Args:
            input (str): The contents of a JS file

        Raises:
            error: TypeError if unable to parse data

        Returns:
            Digraph: The DOT graph of the JS file

        >>> t = Converter()
        >>> results = t.convert("class Patient {\
            constructor(issue) {\
                this.issue = new Object();\
                    }}")
        >>> print(type(results))
        <class 'graphviz.dot.Digraph'>
        """
        try:
            parsed_results = self.parser.parse(file_data)
        except JSParseException:
            raise JSParseException("Failed to parse file")
        try:
            extracted_data = []
            for data in parsed_results.body:
                self.parser.add_class_name(data)
                self.parser.add_attributes(data)
                self.parser.add_methods(data.body.body)
                self.parser.add_relationships(data.body.body)
                extracted_data.append(self.parser.get_extracted_data())
            return DigraphConverter().convert(extracted_data)
        except Exception:
            raise JSParseException("Failed to parse file")

    def save(self, dot_graph: Digraph, filename:
             str, file_format: str) -> None:
        """Renders the DOT graph to select image formats

        Example:
            "bmp", "jpg", "jpeg", "pdf", "png", "svg", "webp"

        Args:
            dot_graph (Digraph): The DOT graph of the parsed JS
            filename (str): The preferred file name
            file_format (str): The preferred file type

        Raises:
            DigraphSaveException: Thrown if unable to save

        >>> t = Converter()
        >>> t.save(Digraph(), "filename", "png")
        """
        try:
            DigraphConverter().render(dot_graph, filename)
        except (Exception, TypeError) as error:
            raise DigraphSaveException("Failed to save digraph")
