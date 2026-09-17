
# Before starting this you should know intermediate python and fundamentals of OOPs
# otherwise its useless to learn this.

# importing BaseModel from pydantic
from pydantic import BaseModel

# Creating class
class ExamplePydanticModel(BaseModel):
    name: str
    age: int
    city: str

# No error example:
me = ExamplePydanticModel(
    name="Sheharyar",
    age=22,
    city="Lahore"
)

# Error example:
# me = ExamplePydanticModel(
#     name="Sheharyar",
#     age='22'
#     city='Lahore'
# )

print(me.name)
print(me.age)
print(me.city
      )