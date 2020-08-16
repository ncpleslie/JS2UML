"""==========================================
; Title:  Abstract JS to UML converter
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from abc import ABC, abstractmethod


class AbstractConverter(ABC):
    @abstractmethod
    def convert(self, input: str):
        raise NotImplementedError("subclasses must override convert()!")

    @abstractmethod
    def save(self, dot_graph, filename: str):
        raise NotImplementedError("subclasses must override save()!")
