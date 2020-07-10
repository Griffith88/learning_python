from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


class ObservableEngine(Engine):
    def __init__(self):
        self.__observers = set()

    def subscribe(self, observer):
        self.__observers.add(observer)

    def unsubscribe(self, observer):
        self.__observers.remove(observer)

    def notify(self, message):
        for observer in self.__observers:
            observer.update(message)