"""==========================================
; Title:  Abstract Read/Write
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from abc import ABC, abstractmethod


class AbstractRead(ABC):
    @abstractmethod
    def load_file(self, input: str):
        """Will load the contents of a file or directory to memory

        Args:
            input (str): The filename or directory
        """
        raise NotImplementedError("subclasses must override load_file()!")
