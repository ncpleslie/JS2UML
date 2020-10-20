"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from graphviz import Digraph, Source
from src.js2uml_constants import JS2UMLConstants
from src.converter.model.abstract_extraction import AbstractExtraction


class DigraphConverter:
    """
    Will convert parsed JavaScript data, in a relevant file format\
         (See JSParser). Converts the parsed JS into a Digraph \
              and can render to select file formats
    """

    def __init__(self):
        self.__dot_graph = Digraph("class_diagram")
        self.__accepted_file_formats = JS2UMLConstants.accepted_file_formats()

    def convert(self, input: list) -> Digraph:
        """Will convert the parsed JS into a Digraph.

        Args:
            input (list): Parsed JS data

        Returns:
            Digraph: DOT graph of the parsed JS

        >>> t = DigraphConverter()
        >>> results = t.convert([{'class_name': 'Patient', \
            'attributes': ['issue'], 'methods': ['constructor'], \
                'edges': {'Object'}}])
        >>> print(type(results))
        <class 'graphviz.dot.Digraph'>
        """
        if input:
            for data in input:
                self.__set_node(data)
                self.__set_edge(data)
            return self.__dot_graph

    def render(self, dot_graph: Digraph, filename="class",
               file_format="png") -> None:
        """Will render the DOT graph in select image formats.

        Example:
            "bmp", "jpg", "jpeg", "pdf", "png", "svg", "webp"

        Raises:
            Exception: Exception is unable to find Dot graph file

        >>> t = DigraphConverter()
        >>> t.render(Digraph(), "filename", "png")
        """
        filename = filename.strip()
        file_format = file_format.strip().lower()
        if file_format not in self.__accepted_file_formats:
            file_format = self.__accepted_file_formats[4]  # png

        source = Source(dot_graph.source,
                        filename=filename, format=file_format)
        source.view()
        self.__delete()

        return

    def __delete(self):
        """Deletes the current stored DOT graph
        """
        self.__dot_graph = Digraph("class_diagram")

    def __set_edge(self, data: AbstractExtraction):
        """Sets the edge. Edges are the relationships to other classes

        Args:
            data (dict): The parsed JS data
        """
        for edge in data.get_relationships():
            self.__dot_graph.edge(data.get_class_name(), edge)

    def __set_node(self, data: AbstractExtraction):
        """Sets the node. Nodes are the classes. Will \
            contain the attributes, methods and name

        Args:
            data (dict): The parsed JS data
        """
        class_name = data.get_class_name()
        attributes = r"\l".join(data.get_attributes())
        methods = r"()\l".join(data.get_methods()) + '()'
        self.__dot_graph.node(
            class_name, f"{{{class_name}|{attributes}|{methods}}}", shape="record",)
