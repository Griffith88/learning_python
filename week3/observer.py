from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    """Наблюдаемый класс"""
    def subscribe(self, subscriber):
        pass

    def unsbuscribe(self, subscriber):
        pass

    def notify(self, message):
        pass

class AbstractObserver(ABC):

    @abstractmethod
    def update(self):



class ShortNotificationPrinter(AbstractObserver):

    def __init__(self, subscriber):
        self.subscriber = set()

    def update(self, message):
        for i in self.subscribers:
           for

class FullNotificationPrinter(AbstractObserver):

    def __init__(self, subscriber):
        self.subscriber = list()

    def update(self):
        pass