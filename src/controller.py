"""==========================================
; Title:  Controller for JS2UML
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""
from argparse import ArgumentParser, Namespace
from errno import EACCES, ENOENT
from src.io.read import Read
from src.console_view.abstract_console_view import AbstractConsoleView
from src.converter.abstract_converter import AbstractConverter
from src.errors.digraph_save_exception import DigraphSaveException
from src.io.config import Config


class Controller:
    """
    The main controller for the JS to UML parser

        Args:
            console_view (AbstractConsoleView): A view class for the
            console screen. Used to grab user input and display messages
            converter (AbstractConverter): The JS parser.
            Used to convert JS to AST, Digraph and output an image file

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
        self._read = Read()
        # Argparser for parsing arguments and flags from command line
        self.__parser = ArgumentParser()
        # JS Parser arguments
        self.__create_parser_args()

    def help(self) -> None:
        """Displays the help screen"""
        self._console_view.show(
            "setup     Set default filenames, directories and filetypes\n"
            "parse     Convert a JavaScript file to a UML class diagram\n"
            "exit      Exits the program")

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

        # Get stored config
        try:
            file_path = Config.get_default_storage_location()
            filename = Config.get_default_filename()
            file_format = Config.get_default_filetype()

        except FileNotFoundError as error:
            self._console_view.show(
                "No config set. Use `setup` to initialize the default configurations.")
        except (IOError, OSError):
            self._console_view.show(
                "Unable to load config file. It may have become corrupt or we don't \
                    have permission to access it. Run setup command again to \
                    fix this issue")

        # Delete stored input if use doesn't want to keep using it
        if file_format and file_path and filename:
            if not self._console_view.get_yes_no_input(
                    f"Found default stored values.\nLocation: "
                    f"{file_path}\nSave as: {filename}\nOutput format:"
                    f"{file_format}\nContinue using these?"):
                file_format = None
                file_path = None
                filename = None

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
        # Ask user what they want the file called
        if not filename:
            filename = self._console_view.get_input("Save file as?")
        # Ask user their preferred file type
        if not file_format:
            file_format = self._console_view.get_input(
                "File format? [bmp, jpg, jpeg, pdf, png, svg, webp]")

        try:
            # Get file
            file = self._read.load_file(file_path)
        except IOError as error:
            self.__file_reader_error_handler(error)

        # Convert file to dot graph
        try:
            dot_graph = self._converter.convert(file)
        except TypeError:
            self._console_view.show(
                "Was that a valid JS file?. Let's try again")
            self.parse()
        except Exception as error:
            # ESPrima will throw a generic error called "Error"
            if type(error).__name__ == "Error":
                self._console_view.show(
                    "Was that a valid JS file?. If it was TS,"
                    "we can't parse that yet. Let's try again")
                self.parse()

        # Save dot graph to set file format
        try:
            self._converter.save(dot_graph, filename, file_format)
        except (DigraphSaveException, TypeError, UnboundLocalError):
            self.__save_error_handler()
        self._console_view.show('JS2UML Conversion Complete')

    def setup(self, args=None) -> None:
        """Guides the user through the set up process. "\
            "Setting default output directory, filetype and name. "\
            "This includes the setup of MongoDB

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

        if not file_path:
            file_path = self._console_view.get_input("Default file location?")

        if not filename:
            filename = self._console_view.get_input("Default file name?")

        if not file_format:
            file_format = self._console_view.get_input(
                "Default file format? [bmp, jpg, jpeg, pdf, png, svg, webp]")

        try:
            Config.set_default_storage_location(file_path)
            Config.set_default_filename(filename)
            Config.set_default_filetype(file_format)
        except (IOError, OSError):
            self._console_view.show(
                "The wrong file type may have been selected or"
                "you may not have permission to open that file."
                "Please try again")
            self.setup()
        self._console_view.show('Setup Complete')

    def __create_parser_args(self) -> None:
        # File/directory location of the JS files
        self.__parser.add_argument("-f")
        # Output file/directory of the UML class diagram
        self.__parser.add_argument("-o")
        # Filetype (image) of the output UML class diagram
        self.__parser.add_argument("-t")

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

    def __parse_args(self, args: str) -> Namespace:
        """Parses arguments passed from the command-line"""
        if args:
            args, _ = self.__parser.parse_known_args(args.split())
            return args

    def __save_error_handler(self) -> None:
        self._console_view.show(
            "I couldn't save that for some reason. "
            "Let's try again"
        )
        self.parse()
