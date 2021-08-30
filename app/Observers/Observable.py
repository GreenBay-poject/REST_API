from abc import abstractmethod, ABC
from app.Observers.Observer import observer


class observable(ABC):
    @abstractmethod
    def attach(self, observer: observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: observer) -> None:
        pass

    @abstractmethod
    def notify(self,message) -> None:
        pass
        