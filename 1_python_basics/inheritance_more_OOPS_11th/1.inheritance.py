

class Employee :
    company = "ITC"
    def show(self) :
        print(f'The name of the employee is {self.name} and the salary of the employee is {self.salary}')

# class Programmer:
#     comany = "ITC infotech"
#     def show(self) :
#         print(f'The name of the employee is {self.name} and the salary of the employee is {self.salary}')

#     def showLanguage(self) :
#         print(f"The name of the employee is {self.name} and our employee is good at {self.language} language")

# Instead of this class we will make it like this:

class Programmer(Employee):
    company = "ITC infotech"
    
    def showLanguage(self) :
        print(f"The name of the employee is {self.name} and our employee is good at {self.language} language")

a = Employee()
b = Programmer
a.show()
b.showLanguage

print(a.company , b.company)