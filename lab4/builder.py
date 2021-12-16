from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  # позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def cup(self) -> None:  # чашка
        pass

    @abstractmethod
    def saucer(self) -> None:  # блюдечко
        pass

    @abstractmethod
    def spoon(self) -> None:  # ложка
        pass


class Service_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = ServiceShop()

    @property  # позволяет превратить метод класса в атрибут класса
    def product(self) -> ServiceShop:
        product = self._product
        self.reset()
        return product

    def cup(self) -> None:
        self._product.add("чашка")

    def saucer(self) -> None:
        self._product.add("блюдечко")

    def spoon(self) -> None:
        self._product.add("ложка")


class ServiceShop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property  # позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяем сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def AnnaLafargue(self) -> None:
        self.builder.cup()
        self.builder.spoon()

    def Luminarc(self) -> None:
        self.builder.saucer()
        self.builder.spoon()


if __name__ == "__main__":
    director = Director()
    builder = Service_Builder()
    director.builder = builder

    print("Анна Лафарг: ")
    director.AnnaLafargue()
    builder.product.list_parts()

    print("\n\nLuminarc: ")
    director.Luminarc()
    builder.product.list_parts()


