class Employee: #class
    numberOfWorkingHours = 40 #class attribute
    salesMadeThisWeek = 6
    def hasAchievedTarget(self): #method
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")

emplyeeOne = Employee() #object
emplyeeTwo = Employee()
emplyeeOne.name = "Johny"
emplyeeTwo.name = "Benny" #instance attribute

Employee.numberOfWorkingHours = 50
print(emplyeeOne.name)
print(emplyeeTwo.name)
