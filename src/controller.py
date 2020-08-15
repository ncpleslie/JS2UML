"""==========================================
; Title:  Controller for JS2UML
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""
from src.io.read_write import ReadWrite
from argparse import ArgumentParser


class Controller():
    def __init__(self, console_view, converter):
        self._console_view = console_view
        self._converter = converter
        self._read_write = ReadWrite()
        self.__parser = ArgumentParser()
        self.__parser.add_argument("-f")
        self.__parser.add_argument("-o")
        self.__parser.add_argument("-t")

    def exit(self):
        """ Exits the programs """
        exit()

    def parse(self, args=None):
        """ 
        This will guide the user through the JS to UML parsing process

        Alternatively, using the following flags:
            -f <filename>
            -o <output>
            -t <filetype>
        """
        # Parse arguments from user, if the exist
        parsed_args = self.__parse_args(args)
        if parsed_args:
            file_path = parsed_args.f
            filename = parsed_args.o
            file_format = parsed_args.t

        # Ask user where the file/directory is
        if not file_path:
            file_path = self._console_view.get_input(
                "Please enter the directory or filename of the JS/TS file(s)")
        try:
            # Get file and join it up with " "
            file = self._read_write.load_file(file_path)
        except IOError:
            self._console_view.show(
                'Was that a valid file or directory? Let\'s try again')
            self.parse()

        # Convert file to dot graph
        try:
            dot_graph = self._converter.convert(file)
        except Exception:  # TODO CHANGE THIS
            self._console_view.show(
                'Was that a valid JS file?. Let\'s try again')
            self.parse()

        # Ask user what they want the file called
        if not filename:
            filename = self._console_view.get_input("Save file as?")
        if not file_format:
            file_format = self._console_view.get_input("File format?")

        # Save dot graph to PDF
        try:
            self._converter.save(dot_graph, filename, file_format)
        except Exception:  # TODO CHANGE THIS
            self._console_view.show(
                'I couldn\'t save that for some reason. Let\'s try again')
            self.parse()

    def setup(self):
        """ Guides the user through the set up process. Setting default output directory, filetype and name. This includes the setup of MongoDB """
        print('not created')

    def __parse_args(self, args):
        if args:
            return self.__parser.parse_args(args.split())
