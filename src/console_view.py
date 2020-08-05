class ConsoleView():
    def __init__(self):
        self.file_path = "tests/index.js"

    def msg(self, message):
        print(message)

    def get_file_path(self):
        return self.file_path
