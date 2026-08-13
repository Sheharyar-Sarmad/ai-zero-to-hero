


class Employee:
    language = 'py' # This is a class attribute:
    salary = 12000000


harry = Employee()
harry.name = "Harry" # This is an object or instance attribute:
print(harry.name , harry.language , harry.salary)
 
rohan = Employee()
rohan.name = "Rohan roro robinson"
print(rohan.salary , rohan.name , rohan.language)

# Here name is the object or instance attribute and the salary and the language are the class attributes as they directly belongs to class