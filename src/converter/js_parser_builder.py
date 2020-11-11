"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from esprima import parse as js_parse
from src.converter.model.body_type_enum import BodyType
from src.errors.parse_exception import ParseException
from src.converter.model.abstract_parser_builder import AbstractParserBuilder
from src.converter.extraction import Extraction


class JSParserBuilder(AbstractParserBuilder):
    """The JavaScript Parser. Will convert the file contents of \
        JavaScript class into class names, \
        attributes, methods and relationships
    """

    def parse(self, file_data: str):
        """Parse a JS file and extract an EST"""
        try:
            return js_parse(file_data)
        except TypeError as error:
            raise error
        except Exception as error:
            raise ParseException("Failed to parse file")

    def add_attributes(self, data: dict) -> list:
        """Get the attributes of the class

        Args:
            data (dict): The AST of the parsed file

        Returns:
            list: A list of strings containing class attributes
        """
        attributes = []
        for body in data.body.body:
            if (
                body.type == BodyType.METHOD.value and
                    body.key.name == BodyType.CONSTRUCTOR.value
            ):
                for aAttribute in body.value.body.body:
                    attributes.append(aAttribute.expression.left.property.name)
        self.extraction[-1].set_attributes(attributes)

    def add_class_name(self, body: dict) -> str:
        """Returns the current class name

        Args:
            body (dict): The AST of the parsed file

        Returns:
            str: Class name
        """
        self.extraction[-1].set_name(body.id.name)

    def add_methods(self, data: dict) -> list:
        """Extracts the method names from a class

        Args:
            data (dict): The AST of the parsed file

        Returns:
            list: List of strings containing extracted method names
        """
        results = [body.key.name for body in data.body.body if body.type ==
                   BodyType.METHOD.value]
        self.extraction[-1].set_methods(results)

    def add_relationships(self, data: dict) -> set:
        """Extracts the relationships with other classes

        Args:
            data (dict): The AST of the parsed file

        Returns:
            set: A set of strings of the relationships to other classes
        """
        relationship = set()
        for body in data.body.body:
            # get relationships in the constructor
            relationship.update(
                deep_body.expression.right.callee.name for deep_body in
                body.value.body.body if deep_body.expression and
                deep_body.expression.right and
                deep_body.expression.right.type ==
                BodyType.NEW.value)

            # Get the relationships from methods
            if (body.type == BodyType.METHOD.value and
                    body.key.name != BodyType.CONSTRUCTOR.value):
                for aMethod in body.value.body.body:
                    if aMethod.declarations:
                        for aDeclaration in aMethod.declarations:
                            if aDeclaration.init.type == BodyType.NEW.value:
                                relationship.add(aDeclaration.init.callee.name)

                    if aMethod.expression and aMethod.expression.arguments:
                        for aArgument in aMethod.expression.arguments:
                            if aArgument.type == BodyType.NEW.value:
                                relationship.add(aArgument.callee.name)
        self.extraction[-1].set_relationships(relationship)
