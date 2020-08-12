"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from esprima import parse


class JSParser():
    def __init__(self):
        self.__parse_results = None
        self.__results = []

    def parse(self, input: str):
        self.__parse_results = parse(input)
        self.__extract_js_data()
        return self.__results

    def __get_attributes(self, data: dict) -> list:
        attributes = []
        for body in data.body.body:
            if body.type == "MethodDefinition" and body.key.name == "constructor":
                for aAttribute in body.value.body.body:
                    attributes.append(
                        aAttribute.expression.left.property.name)
        return attributes

    def __get_methods(self, data: dict) -> list:
        methods = []
        for body in data.body.body:
            if body.type == "MethodDefinition":
                if body.key.name != "constructor":
                    methods.append(body.key.name)
        return methods

    def __get_class(self, body: dict) -> str:
        return body.id.name

    def __get_relationship(self, data: dict) -> list:
        relationship = set()
        for body in data.body.body:
            for deepBody in body.value.body.body:
                if deepBody.expression and deepBody.expression.right and deepBody.expression.right.type == "NewExpression":
                    relationship.add(deepBody.expression.right.callee.name)
        for body in data.body.body:
            if body.type == "MethodDefinition" and body.key.name != "constructor":

                for aMethod in body.value.body.body:
                    if aMethod.declarations:
                        for aDeclaration in aMethod.declarations:
                            if aDeclaration.init.type == "NewExpression":
                                relationship.add(aDeclaration.init.callee.name)

                    if aMethod.expression and aMethod.expression.arguments:
                        for aArgument in aMethod.expression.arguments:
                            if aArgument.type == "NewExpression":
                                relationship.add(aArgument.callee.name)
        return relationship

    def __extract_js_data(self):
        for data in self.__parse_results.body:
            class_name = self.__get_class(data)
            attributes = self.__get_attributes(data)
            methods = self.__get_methods(data)
            relationship = self.__get_relationship(data)
            self.__results.append(
                {"class_name": class_name, "attributes": attributes, "methods": methods, "edges": relationship})

    def __recursive_lookup(self, value, nested_dict, prepath=()):
        for k, v in nested_dict.items():
            path = prepath + (k, v)
            if v == value:  # found value
                return path
            elif hasattr(v, 'items'):  # v is a dict
                p = self.__recursive_lookup(value, v, path)  # recursive call
                if p is not None:
                    return p
