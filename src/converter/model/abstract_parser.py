from abc import ABC, abstractmethod


class AbstractParser(ABC):
    def __init__(self):
        self._results = []

    @abstractmethod
    def parse(self, input: str) -> list:
        ...
