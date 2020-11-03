"""==========================================
; Title:  Abstract JS to UML converter
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from abc import ABC, abstractmethod


class AbstractConverter(ABC):
    """Base for the Converter class. Will convert JS to DOT graph
    """

    @abstractmethod
    def convert(self, file_data: str):
        """Converts a JS file to a DOT graph

        Args:
            input (str): The contents of a JS file

        Raises:
            error: TypeError if unable to parse data

        Returns:
            Digraph: The DOT graph of the JS file
        """
        raise NotImplementedError("subclasses must override convert()!")

    @abstractmethod
    def save(self, dot_graph, filename: str):
        """Renders the DOT graph to select image formats

        Example:
            "bmp", "jpg", "jpeg", "pdf", "png", "svg", "webp"

        Args:
            dot_graph (Digraph): The DOT graph of the parsed JS
            filename (str): The preferred file name
            file_format (str): The preferred file type

        Raises:
            DigraphSaveException: Thrown if unable to save
        """
        raise NotImplementedError("subclasses must override save()!")
