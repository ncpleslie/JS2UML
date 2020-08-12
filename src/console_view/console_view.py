from src.console_view.abstract_console_view import AbstractConsoleView


class ConsoleView(AbstractConsoleView):
    def __init__(self):
        super().__init__()
        self.file_path = "tests/index.js"

    def show(self, message):
        print(message)

    def get_file_path(self):
        return self.file_path
