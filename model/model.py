import esprima


class Model():
    def __init__(self):
        self.parse_results = None

    def parse(self, input):
        self.parse_results = esprima.parseScript(input)

    def get_results(self):
        return self.parse_results
