from ast import parse, walk, ClassDef, Attribute, FunctionDef
from src.converter.model.body_type_enum import BodyType
from src.errors.parse_exception import ParseException
from src.converter.model.abstract_parser_builder import AbstractParserBuilder
from src.converter.extraction import Extraction


class PyParserBuilder(AbstractParserBuilder):
    """
        The Python Parser. Will convert the file contents of \
        Python class into class names, \
        attributes, methods and relationships
    """

    def parse(self, file_data: str):
        """Parse a Py file and extract an EST"""
        try:
            return parse(file_data)
        except Exception as error:
            print(error)
            raise ParseException('Failed to parse file')

    def add_class_name(self, data):
        """Returns the current class name

        Args:
            body (dict): The AST of the parsed file

        Returns:
            str: Class name
        """
        class_name = [c for c in walk(data) if isinstance(c, ClassDef)]
        for name in class_name:
            self.extraction[-1].set_name(name.name)

    def add_attributes(self, data):
        """Get the attributes of the class

        Args:
            data (dict): The AST of the parsed file

        Returns:
            list: A list of strings containing class attributes
        """
        all_attributes = []
        attributes = [c for c in walk(data) if isinstance(c, Attribute)]
        for attribute in attributes:
            all_attributes.append(attribute.attr)
        self.extraction[-1].set_attributes(all_attributes)

    def add_methods(self, data):
        """Extracts the method names from a class

        Args:
            data (dict): The AST of the parsed file

        Returns:
            list: List of strings containing extracted method names
        """
        methods = []
        functions = [c for c in walk(data) if isinstance(c, FunctionDef)]
        for function in functions:
            methods.append(function.name)
        self.extraction[-1].set_methods(methods)

    def add_relationships(self, data):
        """Extracts the relationships with other classes

        Args:
            data (dict): The AST of the parsed file

        Returns:
            set: A set of strings of the relationships to other classes
        """
        self.extraction[-1].set_relationships(set())
