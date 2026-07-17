

class a:
    a = 4

o = a()
print(o.a) # Prints the class attribute becuase instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) # print the instance attribute because instance attriute is present
print(a.a) # print the class attribute