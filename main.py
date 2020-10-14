from js2uml.command_line import CommandLine
from js2uml.controller import Controller
from js2uml.console_view.console_view import ConsoleView
from js2uml.converter.converter import Converter


if __name__ == "__main__":
    controller = Controller(ConsoleView(), Converter())
    CommandLine(controller).cmdloop()
