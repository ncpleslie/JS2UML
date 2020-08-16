from src.command_line import CommandLine
from src.controller import Controller
from src.console_view.console_view import ConsoleView
from src.converter.converter import Converter


if __name__ == "__main__":
    controller = Controller(ConsoleView(), Converter())
    CommandLine(controller).cmdloop()
