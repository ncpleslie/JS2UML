from src.controller import Controller
from src.console_view.console_view import ConsoleView
from src.converter.converter import Converter


if __name__ == "__main__":
    Controller(ConsoleView(), Converter()).run()
