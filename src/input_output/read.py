"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from os import listdir, path
from errno import EACCES
from .abstract_read import AbstractRead
from src.js2uml_constants import JS2UMLConstants


class Read(AbstractRead):
    """Will read files from the device
    """

    def __init__(self):
        self.__default_file_endings = JS2UMLConstants.supported_files()

    def load_file(self, input: str) -> str:
        """Loads a file or directory to memory

        Args:
            input (str): the filename or directory

        Returns:
            str: The file's contents

        >>> t = Read()
        >>> result = t.load_file("test_js/basic/basic.js")
        """
        if path.isfile(input):
            return self.__read_file(input)
        elif path.isdir(input):
            return self.__read_directory(input)
        else:
            raise FileNotFoundError

    def __read_directory(self, directory: str) -> str:
        """Read the contents of a file directory

        Args:
            directory (str): The directory name

        Returns:
            str: All the files contents
        """
        file_contents = ""
        for file in listdir(directory):
            file_contents += self.__read_file(
                f"{path.join(directory, '')}{file}")
        return file_contents

    def __read_file(self, filename: str) -> str:
        """Reads a single file

        Args:
            filename (str): The filename

        Raises:
            io_error: If invalid filetype

        Returns:
            str: The files contents
        """
        try:
            if filename.lower().endswith(self.__default_file_endings):
                with open(filename, "r") as file:
                    return " ".join(file.readlines())
            else:
                print("[ReadWrite Error] Invalid filetype selected")
                io_error = IOError("Invalid filetype selected")
                io_error.errno = EACCES
                raise io_error
        except IOError as error:
            raise error
