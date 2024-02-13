class Observer:

    def _init_(self, observable):
        observable.subscribe(self)


class Observable:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

