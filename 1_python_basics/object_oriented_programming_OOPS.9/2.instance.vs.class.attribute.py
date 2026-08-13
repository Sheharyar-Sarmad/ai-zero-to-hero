
# NOTE: instance attribute take preference over class attributes during assignments and retrieval.

# In simple if you assign a language attribute in the class and then then outside of the class you say example.language = "JavaScript" so it will replace the "py" with "JavaScript". 

class Employee:
    language = 'py' # This is a class attribute:
    salary = 12000000


harry = Employee()
harry.language = "JavaScript" # This is an object or instance attribute:
print(harry.language , harry.salary)
 
# Here name is the object or instance attribute and the salary and the language are the class attributes as they directly belongs to class