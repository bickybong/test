class employee:

    def __init__(self, name): #invokes by default when object created
        self.name = name
        
    def displayEmployeeDetails(self):
        print(self.name)


employee1 = employee("Mark")
employee2 = employee("Jojo")

employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()