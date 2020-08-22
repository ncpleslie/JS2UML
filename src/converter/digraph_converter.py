"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from graphviz import Digraph
from src.js2uml_constants import JS2UMLConstants


class DigraphConverter:
    """
    Will convert parsed JavaScript data, in a relevant file format (See JSParser). Converts the parsed JS into a Digraph and can render to select file formats
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
        >>> results = t.convert([{'class_name': 'Patient', 'attributes': ['issue'], 'methods': ['constructor'], 'edges': {'Object'}}])
        >>> print(results)
        digraph class_diagram {
            Patient [label="{Patient|issue|constructor()}" shape=record]
            Patient -> Object
        }
        """
        for data in input:
            self.__set_node(data)
            self.__set_edge(data)
        return self.__dot_graph

    def render(self, dot_graph: Digraph, filename="class", file_format="png") -> None:
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

        if dot_graph:
            dot_graph.format = file_format
            dot_graph.render(filename)

        elif self.__dot_graph:
            self.__dot_graph.format = file_format
            self.__dot_graph.render(filename)
            self.__delete()
        else:
            raise Exception("Undefined dot graph")

    def __delete(self):
        """Deletes the current stored DOT graph
        """
        self.__dot_graph = Digraph("class_diagram")

    def __set_edge(self, data: dict):
        """Sets the edge. Edges are the relationships to other classes

        Args:
            data (dict): The parsed JS data
        """
        for edge in data["edges"]:
            self.__dot_graph.edge(data["class_name"], edge)

    def __set_node(self, data: dict):
        """Sets the node. Nodes are the classes. Will contain the attributes, methods and name

        Args:
            data (dict): The parsed JS data
        """
        self.__dot_graph.node(
            data["class_name"],
            "{{{className}|{attributes}|{methods}}}".format(
                className=data["class_name"],
                attributes="\l".join(data["attributes"]),
                methods="()\l".join(data["methods"]) + "()",
            ),
            shape="record",
        )
