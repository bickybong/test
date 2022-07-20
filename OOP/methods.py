class employee:
    def employeeDetials(self): #instance method, uses self
        self.name = "Matthew"
        print(self.name)

    @staticmethod
    def welcomeMessage(): #static method doesnt need self
        print("Welcome to our organization!")


employee1 = employee()
employee1.employeeDetials()
employee1.welcomeMessage()
