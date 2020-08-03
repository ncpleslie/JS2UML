from controller.controller import Controller
from console_view.console_view import ConsoleView
from model.model import Model

Controller(ConsoleView(), Model()).run()
