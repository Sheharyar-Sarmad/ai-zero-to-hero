

from typing import List , Union , Tuple , Set
import json

a : Union[int , str , float] = ["ajfd;l" , 12 , 13.2]
print(f"a is working fine:\n{json.dumps(a , indent=2)}")

n : int = 5

name : str = "Sheharyar"

def sum(a: int , b: int) -> int :
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(sum(num1 , num2))


a : List[str , int , str] = ["alice" , 121 ]
print(a)


a : int = []

for integers in range(11) :
    a.append(integers)

print(json.dumps(a , indent=2))