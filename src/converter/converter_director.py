"""==========================================
; Title:  Middleware for JS Parser and Digraph
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""
from src.converter.model.abstract_parser_builder import AbstractParserBuilder
from src.errors.parse_exception import ParseException


class ConverterDirector:
    """Facilitates the conversion of JS files to UML class diagrams
    """

    def __init__(self, builder: AbstractParserBuilder):
        self.builder = builder

    def change_builder(self, builder: AbstractParserBuilder):
        self.builder = builder

    def convert(self, file_data: str):
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
            parsed_results = self.builder.parse(file_data)
        except ParseException:
            raise ParseException("Failed to parse file")
        try:
            for data in parsed_results.body:
                self.builder.create_product()
                self.builder.add_class_name(data)
                self.builder.add_attributes(data)
                self.builder.add_methods(data)
                self.builder.add_relationships(data)
                # extracted_data.append(self.builder.get_extracted_data())
        except Exception:
            raise ParseException("Failed to parse file")
