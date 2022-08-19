class Employee:
    def setNumberWorkingHours(self):
        self.numberWorkingHours = 40

    def displayNumberWorkingHours(self):
        print(self.numberWorkingHours)

class Trainee(Employee):
    def setNumberWorkingHours(self): 
        """ Override previous method """
        self.numberWorkingHours = 45

    def resetNumberWorkingHours(self):
        super().setNumberWorkingHours() 
        """ calls back the ancestor method """


employee = Employee()
employee.setNumberWorkingHours()
print("Number of working hours of employee: ", end="")
employee.displayNumberWorkingHours()

trainee = Trainee()
trainee.setNumberWorkingHours()
print("Number of working hours of trainee: ", end="")
trainee.displayNumberWorkingHours()

trainee.resetNumberWorkingHours()
print("Number of working hours of trainee after reset: ", end="")
trainee.displayNumberWorkingHours()