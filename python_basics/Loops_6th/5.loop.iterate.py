
import json

# For loop iteration with list
my_list = [
    "Harry",
    25,
    3.14,
    True,
    "Python",
    100,
    False,
    9.81,
    "Code",
    42,
    "AI",
    7.5,
    True,
    "Laptop",
    0,
    88.6,
    "Developer",
    False,
    999,
    1.23,
    "Data",
    77,
    "OpenAI",
    5.5,
    True,
    "Keyboard",
    -12,
    6.66,
    "Mouse",
    False,
    2026,
    0.001
]
for item in my_list :
    print(item , "→" , type(item).__name__)

# For loop iteration using tuples
t = (5 , 6 ,7 ,9  ,'Sheharyar' , "sarmad" , "buddi" , 9089 , 283 ,True  , False)
for t_content in t:
    print(json.dumps(t_content), "→", type(t_content).__name__)

# For loop with strings
s = "String"
for stri in s :
    print(stri , "→" , type(stri).__name__)

# For loop iteration with dictionaries

d = {
    "harry":56 ,
    "Harsh":90 ,
    "Sheharyar":100 ,
    "sarmad":100
}

for key , value in d.items() :
    print(key , ":" , value , "→" , type(value).__name__)