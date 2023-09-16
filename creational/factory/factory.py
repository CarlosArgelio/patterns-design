from abc import ABC, abstractmethod


class BaseCar(ABC):
    @abstractmethod
    def show_cost(self):
        pass


class MastodonCar(BaseCar):
    def show_cost(self):
        print("Mastodon Car costs $100")


class RhinoCar(BaseCar):
    def show_cost(self):
        print("Rhino Car costs $200")


class CarFactory(ABC):
    @abstractmethod
    def make_car(self):
        pass


class MastodonCarFactory(CarFactory):
    def make_car(self):
        return MastodonCar()
    

class RhinoCarFactory(CarFactory):
    def make_car(self):
        return RhinoCar()
    

def app_factory(factory):
    car = factory.make_car()
    car.show_cost()
    

def create_factory(type):
    factories = {
        'mastodon': MastodonCarFactory,
        'rhino': RhinoCarFactory
    }

    Factory = factories[type]
    return Factory()


app_factory(create_factory('mastodon'))
app_factory(create_factory('rhino'))