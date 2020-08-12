"""==========================================
; Title:  Controller for JS2UML
; Author: Nick Leslie
; Date:   5/08/2020
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
        file_path = self._console_view.get_input(
            "Please enter the directory or filename of the JS/TS file(s)")

        # Get file and join it up with " "
        file = self._read_write.load_file(file_path)

        # Convert file to dot graph
        dot_graph = self._converter.convert(file)

        # Ask user what they want the file called
        filename = self._console_view.get_input("Save file as?")
        file_format = self._console_view.get_input("File format?")

        # Save dot graph to PDF
        self._converter.save(dot_graph, filename, file_format)
