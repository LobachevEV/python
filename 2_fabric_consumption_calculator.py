from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @abstractmethod
    def calc_fabric_consumption(self) -> float:
        pass


class Coat(Clothes):
    @property
    def type(self) -> str:
        return 'Coat'

    def __init__(self, size: float):
        self.__size = size

    def calc_fabric_consumption(self) -> float:
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def type(self) -> str:
        return 'Suit'

    def __init__(self, height: float):
        self.height = height

    def calc_fabric_consumption(self) -> float:
        return self.height * 2 + 0.3


if __name__ == '__main__':
    clothes = [Coat(9.5), Suit(1.77)]
    for c in clothes:
        print(f'Fabric consumption for {c.type} is {c.calc_fabric_consumption()}')