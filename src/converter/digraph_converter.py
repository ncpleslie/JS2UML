"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from graphviz import Digraph as DG


class DigraphConverter():
    def __init__(self):
        self.__dot_graph = DG("class_diagram")

    def convert(self, input):
        for data in input:
            self.__set_node(data)
            self.__set_edge(data)
        return self.__dot_graph

    def __set_node(self, data):
        self.__dot_graph.node(data['class_name'], "{{{className}|{attributes}|{methods}}}".format(
            className=data['class_name'], attributes="\l".join(data['attributes']), methods="()\l".join(data['methods'])+"()"), shape="record")

    def __set_edge(self, data):
        for edge in data['edges']:
            self.__dot_graph.edge(data['class_name'], edge)

    def render(self, dot_graph, filename):
        if dot_graph:
            dot_graph.render(filename)
        elif self.__dot_graph:
            self.__dot_graph.render(filename)
        else:
            raise Exception('Undefined dot graph')
