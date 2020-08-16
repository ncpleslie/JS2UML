"""==========================================
; Title:  Abstract Read/Write
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from abc import ABC, abstractmethod


class AbstractReadWrite(ABC):
    @abstractmethod
    def load_file(self, input: str):
        raise NotImplementedError("subclasses must override load_file()!")
