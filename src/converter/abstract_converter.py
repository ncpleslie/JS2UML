from abc import ABC, abstractmethod


class AbstractConverter(ABC):
    @abstractmethod
    def convert(self, input: str):
        raise NotImplementedError('subclasses must override convert()!')

    @abstractmethod
    def save(self):
        raise NotImplementedError('subclasses must override save()!')
