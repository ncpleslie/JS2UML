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

    def get_yes_no_input(self, msg=None) -> bool:
        """Get y/n response from user intput

        Args:
            msg ([str], optional): [The message to show the user].\
                 Defaults to None.

        Returns:
            bool: [The yes/no response from the user

        """
        if msg:
            self.show(msg)
        valid = {"yes": True, "y": True, "no": False, "n": False}

        default_output = ' [Y/n] '

        self.show(default_output)

        pick = input().lower()

        while True:
            if pick in valid:
                return valid[pick]
            else:
                self.show(default_output)
