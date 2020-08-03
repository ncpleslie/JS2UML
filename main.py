from controller.controller import Controller
from console_view.console_view import ConsoleView
from model.model import Model


if __name__ == "__main__":
    Controller(ConsoleView(), Model()).run()
