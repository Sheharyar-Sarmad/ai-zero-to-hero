class Employee:
    language = 'py'   # class attribute
    salary = 12000000

    def __init__(self , name , language , salary) : # the methods which starts from double underscore(__) are called as dunder methods in python proggramming and the __init__(self) method functions always automatically called by it self
        self.name = name 
        self.language = language
        self.salary = salary
        print("I am creating an object...")
    
    def getInfo(self):
        print(f"The language is {self.language}.")
        print(f"The salary is {self.salary}")
    
    @staticmethod
    def hello() :
        print("Hello how are you?!")

harry = Employee("Harry" , "JavaScript" , 1200)
harry.getInfo() 
harry.hello()

