"""==========================================
; Title:  Read/Write for JS/TS files
; Author: Nick Leslie
; Date:   5/08/2020
=============================================
"""

from esprima import parse as js_parse
from src.converter.model.body_type_enum import BodyType
from src.errors.js_parse_exception import JSParseException
from src.converter.model.abstract_parser import AbstractParser
from src.converter.js_extraction import JSExtraction


class JSParser(AbstractParser):
    """The JavaScript Parser. Will convert the file contents of \
        JavaScript class into class names, \
        attributes, methods and relationships
    """

    def __init__(self):
        AbstractParser.__init__(self)
        self.__parse_results = None

    def parse(self, input: str) -> list:
        """Parse a JavaScript file's contents and extract
        the class names, attributes, methods and relationships

        Args:
            input (str): The JavaScript file's contents

        Raises:
            error: TypeError if unable to parse the JS file

        Returns:
            dist[]: A list of dicts. Each dict is a class

        >>> t = JSParser()
        >>> results = t.parse("class Patient {\
            constructor(issue) {\
                this.issue = new Object();\
                    }}")
        >>> print(results)
        [{'class_name': 'Patient', 'attributes': ['issue'], 'methods': ['constructor'], 'edges': {'Object'}}]
        """
        if input:
            try:
                self.__parse_results = js_parse(input)
                self.__extract_js_data()
                return self._results
            except TypeError as error:
                raise error
            except Exception as error:
                raise JSParseException("Failed to parse file")

    def __extract_js_data(self) -> None:
        """Loop through each class and extra all attributes from it
        """
        for data in self.__parse_results.body:
            js_extraction = JSExtraction()
            js_extraction.set_name(self.__get_class(data))
            js_extraction.set_attributes(self.__get_attributes(data))
            js_extraction.set_methods(self.__get_methods(data.body.body))
            js_extraction.set_relationships(
                self.__get_relationship(data.body.body))
            self._results.append(js_extraction)

    def __get_attributes(self, data: dict) -> list:
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
        return attributes

    def __get_class(self, body: dict) -> str:
        """Retuns the current class name

        Args:
            body (dict): The AST of the parsed file

        Returns:
            str: Class name
        """
        return body.id.name

    def __get_methods(self, data: dict) -> list:
        """Extracts the method names from a class

        Args:
            data (dict): The AST of the parsed file

        Returns:
            list: List of strings containing extracted method names
        """
        return [body.key.name for body in data if
                body.type == BodyType.METHOD.value]

    def __get_relationship(self, data: dict) -> set:
        """Extracts the relationships with other classes

        Args:
            data (dict): The AST of the parsed file

        Returns:
            set: A set of strings of the relationships to other classes
        """
        relationship = set()
        for body in data:
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
        return relationship
