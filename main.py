from src.command_line import CommandLine
from src.controller import Controller
from src.console_view.console_view import ConsoleView
from src.converter.converter import Converter


if __name__ == "__main__":
    # If args are empty run this
    controller = Controller(ConsoleView(), Converter())
    CommandLine(controller).cmdloop()

    # If args have stuff... do that
