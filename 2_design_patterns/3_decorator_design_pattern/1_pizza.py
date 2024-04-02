from abc import ABC, abstractmethod


class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass


class FarmHouse(BasePizza):
    def cost(self):
        return 200


class Margarita(BasePizza):
    def cost(self):
        return 100


class VegDelight(BasePizza):
    def cost(self):
        return 120


class ToppingDecorator(BasePizza):
    pass


class ExtraCheese(ToppingDecorator):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 10


class Mushroom(ToppingDecorator):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 15


pizaa = Mushroom(ExtraCheese(Margarita()))
print(pizaa.cost())

