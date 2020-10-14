"""==========================================
; Title:  Middleware for JS Parser and Digraph
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""
from graphviz import Digraph
from js2uml.converter.abstract_converter import AbstractConverter
from js2uml.converter.js_parser import JSParser
from js2uml.converter.digraph_converter import DigraphConverter
from js2uml.errors.digraph_save_exception import DigraphSaveException


class Converter(AbstractConverter):
    """Facilitates the conversion of JS files to UML class diagrams
    """

    def convert(self, input: str) -> Digraph:
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
            parsed_js = JSParser().parse(input)
            return DigraphConverter().convert(parsed_js)
        except TypeError as error:
            raise error

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
        except Exception as error:
            raise DigraphSaveException("Failed to save digraph")
