from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self) -> None:
        pass


class Tea(HotDrink):
    def consume(self) -> None:
        print('This is tea')


class Coffee(HotDrink):
    def consume(self) -> None:
        print('This is coffee')


class HotDrinkFactory(ABC):
    def prepare(self, amount: int) -> HotDrink:
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> Tea:
        print(f'prepare tea, {amount} ml')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> Coffee:
        print(f'prepare coffee, {amount} ml')
        return Coffee()


def make_drink(drink_type: str) -> HotDrink:
    if drink_type == 'tea':
        return TeaFactory().prepare(200)
    elif drink_type == 'coffee':
        return CoffeeFactory().prepare(50)


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.title()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self) -> HotDrink:
        print('Available Drinks: ')
        for f in self.factories:
            print(f[0])
        idx = int(input(f'Please pick drink 0-{len(self.factories) - 1}:'))
        amount = int(input('Specify amount: '))
        return getattr(self.factories[idx][1], 'prepare')(amount)


if __name__ == '__main__':
    # entry = 'Choose drink'
    # drink = make_drink(entry)
    # drink.consume()
    hdm = HotDrinkMachine()
    hdm.make_drink()
