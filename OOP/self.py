class employee:
    def employeeDetials(self):
        self.name = "Matthew"
        print(f"Name = {self.name}")
        age = 30
        print((f"age = {age}"))

    def printEmployeeDetials(self):
        print((f"age = {age}")) #age is method scope so doesnt work

employee1 = employee()
employee1.printEmployeeDetials()
