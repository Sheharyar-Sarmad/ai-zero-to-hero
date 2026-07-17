class Employee:
    language = 'py'   # class attribute
    salary = 12000000

    def getInfo(self):
        print(f"The language is {self.language}.")
        print(f"The salary is {self.salary}")
    
    def greet(self) :
        print(f"Good day employee({self.name})")

    @staticmethod
    def hello() :
        print("Hello how are you?!")

harry = Employee()
harry.language = "JavaScript"   # instance attribute (overrides class attribute)
harry.name = "Harry"
print(harry.language, harry.salary)

harry.greet()
harry.hello()
harry.getInfo() # This converts into like this:
# Employee.getLanguage(harry) thats why we have to pass the self argument into the function written in the class so it should not throw the error of argument.