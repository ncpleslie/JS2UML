"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from errno import EACCES, ENOENT
from os import listdir, path

from src.io.abstract_read_write import AbstractReadWrite


class ReadWrite(AbstractReadWrite):
    """
    """

    def __init__(self):
        self.__default_file_endings = ('js', 'ts')
        self.__default_directory_endings = ('/', '\\')

    def load_file(self, input: str) -> str:
        if path.isfile(input):
            return self.__read_file(input)
        elif path.isdir(input):
            return self.__read_directory(input)

    def __read_directory(self, directory: str) -> str:
        file_contents = ''
        for file in listdir(directory):
            file_contents += self.__read_file(
                f"{path.join(directory, '')}{file}")
        return file_contents

    def __read_file(self, filename: str) -> str:
        try:
            if filename.lower().endswith(self.__default_file_endings):
                with open(filename, 'r') as file:
                    return " ".join(file.readlines())
            else:
                print(
                    '[ReadWrite Error] Invalid filetype selected')
                raise Exception('Invalid filetype selected')
        except IOError as error:
            if error.errno == EACCES:
                print(
                    '[ReadWrite Error] File is present but it unreadable')
                raise Exception('File is present but it unreadable')
            if error.errno == ENOENT:
                print('[ReadWrite Error] File not found')
                raise Exception('File not found')