

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def make_sound(self) -> None:
        ...

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> None:
        print(f"{self.name} says Meow!")

cat: Cat = Cat("Whiskers")
cat.make_sound()