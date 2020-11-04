from abc import ABC, abstractmethod
from src.converter.extraction import Extraction


class AbstractParserBuilder(ABC):
    def __init__(self):
        self.extraction = Extraction()

    def get_extracted_data(self) -> Extraction:
        results = self.extraction
        self.extraction = Extraction()
        return results

    @abstractmethod
    def parse(self, file_data: str):
        raise NotImplementedError()

    @abstractmethod
    def add_class_name(self, data):
        raise NotImplementedError()

    @abstractmethod
    def add_attributes(self, data):
        raise NotImplementedError()

    @abstractmethod
    def add_methods(self, data):
        raise NotImplementedError()

    @abstractmethod
    def add_relationships(self, data):
        raise NotImplementedError()
