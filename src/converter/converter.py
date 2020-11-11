from graphviz import Digraph
from src.converter.model.iconverter import IConverter
from src.converter.digraph_converter import DigraphConverter
from src.errors.digraph_save_exception import DigraphSaveException
from src.converter.converter_director import ConverterDirector
from src.converter.model.abstract_parser_builder import AbstractParserBuilder


class Converter(IConverter):
    def __init__(self, parser_builder: AbstractParserBuilder):
        self.parser_builder = parser_builder
        self.converter_director = ConverterDirector(self.parser_builder)

    def change_builder(self, parser_builder: AbstractParserBuilder):
        self.converter_director.change_builder(parser_builder)

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

        self.converter_director.convert(file_data)
        results = self.parser_builder.get_extracted_data()
        return DigraphConverter().convert(results)

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
        except (Exception, TypeError):
            raise DigraphSaveException("Failed to save digraph")
