"""
Абстрактный класс ItemFabric: Этот класс представляет собой "создателя" в паттерне Фабричный метод. 
Он имеет абстрактный метод create_item(), который предназначен для переопределения в подклассах. 
Я упростила реализацию, позволив ItemFabric принимать конкретный класс 
предмета в качестве аргумента, что делает создание подклассов необязательным.

Метод create_item(): Этот метод является фабричным методом. Он отвечает за создание объекта. 
В моем коде этот метод создает и возвращает экземпляр класса предмета, переданного ItemFabric 
при инициализации.

Классы GoldReward, GemReward, SilverReward и BronzeReward: Эти классы представляют собой 
"конкретные продукты" в паттерне Фабричный метод. Они реализуют интерфейс IGameItem и имеют 
метод open(), который вызывается после создания объекта.

Я используею параметризованный конструктор вместо подклассов для задания конкретного продукта. 
Это делает код более компактным и уменьшает необходимость в создании множества 
подклассов для каждого типа предмета.


"""



from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):

    def __init__(self, item_class):
        self._item_class = item_class

    @abstractmethod
    def create_item(self):
        return self._item_class()

    def open_reward(self):
        print('Create new bag or chest')
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class SilverReward(IGameItem):
    def open(self):
        print('Silver')


class BronzeReward(IGameItem):
    def open(self):
        print('Bronze')


if __name__ == '__main__':
    lst = [ItemFabric(GoldReward), ItemFabric(GemReward), ItemFabric(SilverReward), ItemFabric(BronzeReward)]
    for i in range(20):
        generator = choice(lst)
        generator.open_reward()
