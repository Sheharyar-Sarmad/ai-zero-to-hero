

class Employee :
    company = "ITC"
    def show(self , name , salary) :
        self.name = name
        self.salary = salary
        print(f'\nThe name of the employee is {self.name} and the salary of the employee is {self.salary}\n')

class Coder:
    language = "Python(py)"
    
    def printLanguages(self , language) :
        self.language = language
        print(f'\nOut of all the languages, here is your language {self.language}\n')

class Programmer(Employee , Coder):
    company = "ITC infotech"
    
    def showLanguage(self , name , language) :
        self.name = name
        self.language = language
        print(f"\nThe name of the employee is {self.name} and our employee is good at {self.language} language\n")

a = Employee()
b = Programmer()
c = Coder()

a.show("Sheharyar" , 120000)
b.showLanguage("Sheharyar" , "Python(py)")
c.printLanguages("Javascript")
# print(a.company , b.company)