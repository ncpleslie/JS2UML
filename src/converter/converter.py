from src.converter.abstract_converter import AbstractConverter
from src.converter.js_parser import JSParser
from src.converter.digraph_converter import DigraphConverter


class Converter(AbstractConverter):
    def __init__(self):
        self._js_parser = JSParser()
        self._digraph = DigraphConverter()
        self._dot_graph = None

    def convert(self, input: str):
        parsed_js = self._js_parser.parse(input)
        self._dot_graph = self._digraph.convert(parsed_js)
        return self._dot_graph

    def save(self, dot_graph, filename):
        self._digraph.render(self._dot_graph, filename)
