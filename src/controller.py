class Controller():
    def __init__(self, console_view, converter):
        self._console_view = console_view
        self._converter = converter

    def run(self):
        self._console_view.show("Please enter a file path")
        file_path = self._console_view.get_file_path()
        file = " ".join(open(file_path).readlines())
        dot_graph = self._converter.convert(file)
        self._console_view.show(dot_graph)
        self._converter.save(dot_graph, "diagram")
