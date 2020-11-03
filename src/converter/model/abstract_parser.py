from abc import ABC, abstractmethod
from src.converter.extraction import Extraction


class AbstractParser(ABC):
    def __init__(self):
        self.extraction = Extraction()

    def get_extracted_data(self) -> Extraction:
        return self.extraction

    @abstractmethod
    def parse(self, file_data: str):
        ...

    @abstractmethod
    def add_class_name(self, data):
        ...

    @abstractmethod
    def add_attributes(self, data):
        ...

    @abstractmethod
    def add_methods(self, data):
        ...

    @abstractmethod
    def add_relationships(self, data):
        ...
