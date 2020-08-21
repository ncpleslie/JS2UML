"""==========================================
; Title:  Console View
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from src.console_view.abstract_console_view import AbstractConsoleView


class ConsoleView(AbstractConsoleView):
    """For display and extract user input on the console
    """

    def show(self, msg: str) -> None:
        """Will display a string on the console screen

        Args:
            msg (str): What will be shown in the console
        >>> t = ConsoleView()
        >>> t.show("test")
        test
        """
        print(msg)

    def get_input(self, msg: str) -> str:
        """Will display a message and return the string response from the user

        Args:
            msg (str): The message that will be shown to the user

        Returns:
            str: The users response
        >>> t = ConsoleView()
        >>> t.get_input("test")
        test
        ''
        """
        self.show(msg)
        return input()
