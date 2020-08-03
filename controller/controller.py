class Controller():
    def __init__(self, console_view, model):
        self.console_view = console_view
        self.model = model

    def run(self):
        self.console_view.msg(self.model.get_value())
