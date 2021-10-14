from abc import abstractmethod, ABC


class observer(ABC):
    @abstractmethod
    def update(self):
        pass
        