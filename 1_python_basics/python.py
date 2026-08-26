

# # First python program

# print("hello world!")

# # Variables: 

# _ = 12
# a = 12
# b = 12

# # This is called as an f string
# print(f"_ + a = {_+a}")

# a = "str"

# print(a)

# Mathematical operations: 

# a = 12
# b = 20

# print(a+b)
# print(a-b)
# print(a-b)
# print(a-b)
# print(a-b)

# data types
# str, int, float, list, dict, bool

# a: str = "1" # '1'
# a: int = int(a) # a: int = "1" ko integer mai convert kardo

# print(type(a))


# a: str = "123123123"
# a: int = int(a)
# # print(a)

# a: str = "12"
# a: int = int(a)

# print(type(a))

from typing import Literal

class Validation:
    def __init__(self):
        pass

    def is_guns_names_len_0(self, names: list[str]) -> bool:
        return len(names) == 0

    def is_guns_name_legal_
    


class Logic(Validation):
    def __init__(self):
        super().__init__()

class BattleRoyal(Logic):
    def __init__(
            self,
            name: str, 
            health: float = 100,
            guns: dict[str],
    ):
        super().__init__
        self.name: str = name 
        self.health: float = health
        self.guns: dict[str] = guns

        def create_guns(
                self,
                names: list[str]
        ) -> list | None :
            try: 
                self.names: list[str] = names
                if (
                    self.is_guns_names_len_0(self.names) or
                )
            except Exception as err: 
                pass