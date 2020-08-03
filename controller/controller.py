class Controller():
    def __init__(self, console_view, model):
        self.console_view = console_view
        self.model = model

    def run(self):
        self.console_view.msg("Please enter a file path")
        file_path = self.console_view.get_file_path()
        file = " ".join(open(file_path).readlines())
        self.model.parse(file)
        self.console_view.msg(self.model.get_results())
