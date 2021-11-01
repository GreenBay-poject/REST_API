from app.Observers.Observable import observable
from app.Observers.Observer import observer

class Post_Observable(observable):
    observers= []
    

    def attach(self, observer: observer) -> None:
        print("Subject: Attached an observer.")
        self.observers.append(observer)

    def detach(self, observer: observer) -> None:
        self.observers.remove(observer)


    def notify(self,message) -> None:
        print("Subject: Notifying observers...")
        for observer in self.observers:
            observer.update(message)