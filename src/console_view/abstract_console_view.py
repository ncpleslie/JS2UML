"""==========================================
; Title:  Abstract Console View
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from abc import ABC, abstractmethod


class AbstractConsoleView(ABC):
    @abstractmethod
    def show(self, msg: str):
        raise NotImplementedError('subclasses must override show()!')

    @abstractmethod
    def get_input(self, msg: str):
        raise NotImplementedError('subclasses must override get_input()!')
