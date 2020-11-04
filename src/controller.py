"""==========================================
; Title:  Controller for JS2UML
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""
from argparse import ArgumentParser, Namespace
from errno import EACCES, ENOENT
from src.input_output.read import Read
from src.console_view.iconsole_view import IConsoleView
from src.converter.model.iconverter import IConverter
from src.errors.digraph_save_exception import DigraphSaveException
from src.errors.parse_exception import ParseException
from src.input_output.config import Config
from src.parser_factory.abstract_parser_creator import AbstractParserCreator


class Controller:
    """
    The main controller for the JS to UML parser

        Args:
            console_view (IConsoleView): A view class for the
            console screen. Used to grab user input and display messages
            converter (IConverter): The JS parser.
            Used to convert JS to AST, Digraph and output an image file

        Example:
            `Controller(View(), Converter()).parse()`
    """

    def __init__(self, console_view: IConsoleView,
                 converter: IConverter, changer: AbstractParserCreator):
        # Console View
        self._console_view = console_view
        # JS Parser
        self._converter = converter
        # Parser changer
        self._changer = changer
        # File/directory reader
        self._read = Read()
        # Argparser for parsing arguments and flags from command line
        self.__parser = ArgumentParser()
        # JS Parser arguments
        self.__create_parser_args()

    def help(self) -> None:
        """Displays the help screen"""
        self._console_view.show(
            "Change which files can be parsed. Currently supported are JavaScript and Python\n"
            "setup     Set default filenames, directories and filetypes\n"
            "parse     Convert a JavaScript file to a UML class diagram\n"
            "exit      Exits the program")

    def exit(self) -> None:
        """Exits the programs"""
        exit()

    def change(self) -> None:
        """Changes which parser is set.
        Will swap between JS parser or Py parser"""
        self._converter.change_builder(self._changer.pick_parser_factory())

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

        if not args:
            # Get stored config
            try:
                file_path = Config.get_default_storage_location()
                filename = Config.get_default_filename()
                file_format = Config.get_default_filetype()

            except FileNotFoundError as error:
                self._console_view.show(
                    "No config set. Use `setup` to initialize the default configurations.")

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
        else:
            parsed_args = self.__parse_args(args)
            file_path = parsed_args.f
            filename = parsed_args.o
            file_format = parsed_args.t

        # Ask user where the file/directory is
        if not file_path:
            file_path = self._console_view.get_input(
                "Please enter the directory or "
                "filename of the JS/PY file(s)"
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
            loaded_file = self._read.load_file(file_path)
        except (IOError, FileNotFoundError) as error:
            self.__file_reader_error_handler(error)
            return

        # Convert file to dot graph
        try:
            dot_graph = self._converter.convert(loaded_file)
        except ParseException:
            self._console_view.show(
                'Unable to parse file. Was it a valid JS or PY file?')
            return

        # Save dot graph to set file format
        try:
            self._converter.save(dot_graph, filename, file_format)
        except (DigraphSaveException, TypeError, UnboundLocalError) as error:
            print(error)
            self.__save_error_handler()

        self._console_view.show('JS2UML Conversion Complete')
        return

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
                "The wrong file type may have been selected or "
                "you may not have permission to open that file. "
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
        return

    def __parse_args(self, args: str) -> Namespace:
        """Parses arguments passed from the command-line"""
        if args:
            parsed_args, _ = self.__parser.parse_known_args(args.split())
            return parsed_args

    def __save_error_handler(self) -> None:
        self._console_view.show(
            "I couldn't save that for some reason. "
            "Let's try again"
        )
        return
