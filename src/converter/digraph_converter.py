"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from graphviz import Digraph


class DigraphConverter:
    def __init__(self):
        self.__dot_graph = Digraph("class_diagram")
        self.__accepted_file_formats = [
            "bmp",
            "jpg",
            "jpeg",
            "pdf",
            "png",
            "svg",
            "webp",
        ]

    def convert(self, input: list) -> Digraph:
        for data in input:
            self.__set_node(data)
            self.__set_edge(data)
        return self.__dot_graph

    def __delete(self):
        self.__dot_graph = Digraph("class_diagram")

    def __set_node(self, data: dict):
        self.__dot_graph.node(
            data["class_name"],
            "{{{className}|{attributes}|{methods}}}".format(
                className=data["class_name"],
                attributes="\l".join(data["attributes"]),
                methods="()\l".join(data["methods"]) + "()",
            ),
            shape="record",
        )

    def __set_edge(self, data: dict):
        for edge in data["edges"]:
            self.__dot_graph.edge(data["class_name"], edge)

    def render(self, dot_graph: Digraph, filename="class", file_format="png"):
        filename = filename.strip()
        file_format = file_format.strip().lower()
        if file_format not in self.__accepted_file_formats:
            file_format = "png"

        if dot_graph:
            dot_graph.format = file_format
            dot_graph.render(filename)

        elif self.__dot_graph:
            self.__dot_graph.format = file_format
            self.__dot_graph.render(filename)
            self.__delete()
        else:
            raise Exception("Undefined dot graph")
