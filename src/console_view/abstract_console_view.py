"""==========================================
; Title:  Abstract Console View
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from abc import ABC, abstractmethod


class AbstractConsoleView(ABC):
    """For display and extract user input on the console
    """

    @abstractmethod
    def show(self, msg: str):
        """Will display a string on the console screen

        Args:
            msg (str): What will be shown in the console
        """
        raise NotImplementedError("subclasses must override show()!")

    @abstractmethod
    def get_input(self, msg: str):
        """Will display a message and return the string response from the user

        Args:
            msg (str): The message that will be shown to the user

        Returns:
            str: The users response
        """
        raise NotImplementedError("subclasses must override get_input()!")
