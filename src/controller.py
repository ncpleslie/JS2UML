"""==========================================
; Title:  Controller for JS2UML
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from src.io.read_write import ReadWrite


class Controller():
    def __init__(self, console_view, converter):
        self._console_view = console_view
        self._converter = converter
        self._read_write = ReadWrite()

    def run(self):
        # Ask user where the file/directory is
        self._console_view.show("Please enter a file path")
        file_path = self._console_view.get_input()

        # Get file and join it up with " "
        file = self._read_write.load_file(file_path)

        # Convert file to dot graph
        dot_graph = self._converter.convert(file)

        # Show dot graph to console
        self._console_view.show(dot_graph)

        # Save dot graph to PDF
        self._converter.save(dot_graph, "diagram")
