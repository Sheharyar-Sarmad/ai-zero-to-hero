
class Employee:
    def __init__(self):
        self.salary = 234
        self.increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Calculate increment percentage from new salary
        self.increment = ((new_salary - self.salary) / self.salary) * 100

e = Employee()

number = int(input("Enter your current salary: "))
e.salaryAfterIncrement = number

print("New Increment:", round(e.increment , 2))
print("New Salary:", round(e.salaryAfterIncrement , 2))