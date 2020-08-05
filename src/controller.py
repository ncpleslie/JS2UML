from src.js_parser import JSParser
from src.digraph import Digraph


class Controller():
    def __init__(self, console_view):
        self.console_view = console_view
        self.js_parser = JSParser()
        self.digraph = Digraph()

    def run(self):
        self.console_view.msg("Please enter a file path")
        file_path = self.console_view.get_file_path()
        file = " ".join(open(file_path).readlines())
        parsed_js = self.js_parser.parse(file)
        dot_graph = self.digraph.convert(parsed_js)
        self.console_view.msg(dot_graph)
        self.digraph.render()
