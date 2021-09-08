from abc import abstractmethod, ABC


class Report(ABC):
    mlmodel=None
    
    def __init__(self,mlmodel):
        self.mlmodel=mlmodel
        
    @abstractmethod
    def set_urls(self, urls_array):
        pass

    @abstractmethod
    def generate_report(self):
        pass

        