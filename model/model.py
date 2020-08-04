import esprima
from graphviz import Digraph
from subprocess import call


class Model():
    def __init__(self):
        self.parse_results = None
        self.dot = Digraph("class")

    def parse(self, input):
        self.parse_results = esprima.parse(input)
        self.find_class()

    def get_results(self):
        return self.parse_results

    def find_class(self):
        for aClass in self.parse_results.body:
            attributes = []
            methods = []
            for aBody in aClass.body.body:

                if aBody.type == "MethodDefinition":
                    if aBody.key.name == "constructor":
                        for aAttribute in aBody.value.params:
                            attributes.append(aAttribute.name)
                    else:
                        methods.append(aBody.key.name)
            self.dot.node(aClass.id.name, "{{{className}|{attributes}|{methods}}}".format(
                className=aClass.id.name, attributes="\l".join(attributes), methods="()\l".join(methods)+"()"), shape="record")
        self.dot.render('class.dot')
