from graphviz import Digraph as DG


class Digraph():
    def __init__(self):
        self.__dot_graph = DG("class")

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

    def render(self):
        self.__dot_graph.render('class')
