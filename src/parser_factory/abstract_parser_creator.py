from abc import ABC, abstractmethod
from src.converter.model.abstract_parser_builder import AbstractParserBuilder


class AbstractParserCreator(ABC):

    @abstractmethod
    def pick_parser_factory(self) -> AbstractParserBuilder:
        raise NotImplementedError
