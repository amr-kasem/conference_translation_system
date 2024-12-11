from abc import ABC, abstractmethod
class Usecase(ABC):
    @abstractmethod
    def __call__(self,parameters)  -> None:
        pass