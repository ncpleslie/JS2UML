from ast import parse, walk, ClassDef, Attribute, FunctionDef
from src.converter.model.body_type_enum import BodyType
from src.errors.parse_exception import ParseException
from src.converter.model.abstract_parser_builder import AbstractParserBuilder
from src.converter.extraction import Extraction


class PyParserBuilder(AbstractParserBuilder):

    def parse(self, file_data: str):
        try:
            return parse(file_data)
        except Exception as error:
            print(error)
            raise ParseException('Failed to parse file')

    def add_class_name(self, data):
        class_name = [c for c in walk(data) if isinstance(c, ClassDef)]
        for name in class_name:
            self.extraction.set_name(name.name)

    def add_attributes(self, data):
        all_attributes = []
        attributes = [c for c in walk(data) if isinstance(c, Attribute)]
        for attribute in attributes:
            all_attributes.append(attribute.attr)
        self.extraction.set_attributes(all_attributes)

    def add_methods(self, data):
        methods = []
        functions = [c for c in walk(data) if isinstance(c, FunctionDef)]
        for function in functions:
            methods.append(function.name)
        self.extraction.set_methods(methods)

    def add_relationships(self, data):
        self.extraction.set_relationships(set())
