"""==========================================
; Title:  Console View
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from src.console_view.abstract_console_view import AbstractConsoleView


class ConsoleView(AbstractConsoleView):
    def show(self, message):
        print(message)

    def get_input(self):
        return input()
