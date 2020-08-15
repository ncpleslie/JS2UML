"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from esprima import parse
from src.models.body_type import BodyType


class JSParser():
    def __init__(self):
        self.__parse_results = None
        self.__results = []

    def parse(self, input: str):
        try:
            self.__parse_results = parse(input)
            self.__extract_js_data()
            return self.__results
        except:
            raise Exception('Failed to parse JS')

    def __get_attributes(self, data: dict) -> list:
        attributes = []
        for body in data.body.body:
            if body.type == BodyType.METHOD.value and body.key.name == BodyType.CONSTRUCTOR.value:
                for aAttribute in body.value.body.body:
                    attributes.append(
                        aAttribute.expression.left.property.name)
        return attributes

    def __get_methods(self, data: dict) -> list:
        methods = []
        for body in data.body.body:
            if body.type == BodyType.METHOD.value:
                if body.key.name != BodyType.CONSTRUCTOR.value:
                    methods.append(body.key.name)
        return methods

    def __get_class(self, body: dict) -> str:
        return body.id.name

    def __get_relationship(self, data: dict) -> list:
        relationship = set()
        for body in data.body.body:
            for deepBody in body.value.body.body:
                if deepBody.expression and deepBody.expression.right and deepBody.expression.right.type == BodyType.NEW.value:
                    relationship.add(deepBody.expression.right.callee.name)
        for body in data.body.body:
            if body.type == BodyType.METHOD.value and body.key.name != BodyType.CONSTRUCTOR.value:

                for aMethod in body.value.body.body:
                    if aMethod.declarations:
                        for aDeclaration in aMethod.declarations:
                            if aDeclaration.init.type == BodyType.NEW.value:
                                relationship.add(aDeclaration.init.callee.name)

                    if aMethod.expression and aMethod.expression.arguments:
                        for aArgument in aMethod.expression.arguments:
                            if aArgument.type == BodyType.NEW.value:
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
