from abc import ABC, abstractmethod


class AbstractExtraction(ABC):

    def __init__(self):
        self.__class_name = None
        self.__methods = None
        self.__attributes = None
        self.__relationships = None

    def set_name(self, name: str) -> None:
        self.__class_name = name

    def set_methods(self, methods: list) -> None:
        self.__methods = methods

    def set_attributes(self, attributes: list) -> None:
        self.__attributes = attributes

    def set_relationships(self, relationships: list) -> None:
        self.__relationships = relationships

    def get_class_name(self) -> str:
        return self.__class_name

    def get_methods(self) -> list:
        return self.__methods

    def get_attributes(self) -> list:
        return self.__attributes

    def get_relationships(self) -> set:
        return self.__relationships
