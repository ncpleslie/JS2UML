from abc import ABC, abstractmethod


class AbstractConsoleView(ABC):
    @abstractmethod
    def show(self, msg: str):
        raise NotImplementedError('subclasses must override show()!')
