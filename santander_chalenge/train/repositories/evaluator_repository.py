from abc import abstractmethod, ABC

class Evaluator(ABC):

    @abstractmethod
    def evaluate(self):
        pass
