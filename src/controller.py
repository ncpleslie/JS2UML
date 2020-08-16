"""==========================================
; Title:  Controller for JS2UML
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""
from argparse import ArgumentParser, Namespace
from errno import EACCES, ENOENT
from src.io.read_write import ReadWrite
from src.console_view.abstract_console_view import AbstractConsoleView
from src.converter.abstract_converter import AbstractConverter


class Controller:
    """
    The main controller for the JS to UML parser

        Args:
            console_view (AbstractConsoleView): A view class for the console screen. Used to grab user input and display messages
            converter (AbstractConverter): The JS parser. Used to convert JS to AST, Digraph and output an image file

        Example:
            `Controller(View(), Converter()).parse()`
    """

    def __init__(self, console_view: AbstractConsoleView,
                 converter: AbstractConverter):
        # Console View
        self._console_view = console_view
        # JS Parser
        self._converter = converter
        # File/directory reader
        self._read_write = ReadWrite()
        # Argparser for parsing arguments and flags from command line
        self.__parser = ArgumentParser()
        # File/directory location of the JS files
        self.__parser.add_argument("-f")
        # Output file/directory of the UML class diagram
        self.__parser.add_argument("-o")
        # Filetype (image) of the output UML class diagram
        self.__parser.add_argument("-t")

    def exit(self) -> None:
        """Exits the programs"""
        exit()

    def parse(self, args=None) -> None:
        """
        This will guide the user through the JS to UML parsing process

        Alternatively, using the following flags:
            -f <filename>
            -o <output>
            -t <filetype>
        """
        file_path = None
        filename = None
        file_format = None
        parsed_args = None

        # Parse arguments from user, if the exist
        if args:
            parsed_args = self.__parse_args(args)
        if parsed_args:
            file_path = parsed_args.f
            filename = parsed_args.o
            file_format = parsed_args.t

        # Ask user where the file/directory is
        if not file_path:
            file_path = self._console_view.get_input(
                "Please enter the directory or "
                "filename of the JS/TS file(s)"
            )
        try:
            # Get file and join it up with " "
            file = self._read_write.load_file(file_path)
        except IOError as error:
            self.__file_reader_error_handler(error)

            # Convert file to dot graph
        try:
            dot_graph = self._converter.convert(file)
        except TypeError:
            self._console_view.show(
                "Was that a valid JS file?. Let's try again")
            self.parse()

        # Ask user what they want the file called
        if not filename:
            filename = self._console_view.get_input("Save file as?")
        if not file_format:
            file_format = self._console_view.get_input("File format?")

        # Save dot graph to set file format
        try:
            self._converter.save(dot_graph, filename, file_format)
        except Exception:  # TODO CHANGE THIS
            self._console_view.show(
                "I couldn't save that for some reason. "
                "Let's try again"
            )
            self.parse()
        self.exit()

    def __file_reader_error_handler(self, error):
        if error.errno == EACCES:
            self._console_view.show(
                "[ReadWrite Error] File is present but "
                "it unreadable. Let's try again"
            )
        if error.errno == ENOENT:
            self._console_view.show(
                "[ReadWrite Error] File not found. "
                "Did you select the right file or path?"
            )
        self.parse()

    def setup(self) -> None:
        """Guides the user through the set up process. "\
            "Setting default output directory, filetype and name. "\
            "This includes the setup of MongoDB"""
        print("not created")

    def __parse_args(self, args: str) -> Namespace:
        """Parses arguments passed from the command-line"""
        if args:
            return self.__parser.parse_args(args.split())
