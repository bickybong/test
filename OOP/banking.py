from abc import ABCMeta, abstractmethod
from random import randint

class ABC(metaclass = ABCMeta):
    @abstractmethod
    def createAccount(self, name, initialDeposit):
        return 0
    def authenticate(self, name, accountNumber):
        return 0
    def withdraw(self, withdrawlAmount):
        return 0
    def deposit(self, depositAmount):
        return 0
    def displayBalance(self):
        return 0

class SavingsAccount:
    def __init__(self):
        self.savingsAccount = {}
    
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print(self.savingsAccount)
        print(f"Your account has been created, account number is {self.accountNumber}")

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            print("Second check")
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else: 
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawlAmount):
        if withdrawlAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawlAmount
            print(f"Withdrew successful, updated balance is {self.savingsAccount[self.accountNumber][1]}")

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print(f"Deposit successful, updated balance is {self.savingsAccount[self.accountNumber][1]}")


    def displayBalance(self):
        print(f"Balance is {self.savingsAccount[self.accountNumber][1]}")


savings = SavingsAccount()

while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        name = input("Enter your name ")
        deposit = int(input("Enter the initial deposit "))
        savings.createAccount(name,deposit)
    elif userChoice is 2:
        name = input("Enter your name ")
        acc = int(input("Enter your account number "))
        authenticationStatus = savings.authenticate(name, acc)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to check balance")
                print("Enter 4 to return to previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    withdrawAmt = int(input("Enter amount to be withdrawn "))
                    savings.withdraw(withdrawAmt)
                elif userChoice is 2:
                    depositAmt = int(input("Enter amount to be deposited "))
                    savings.deposit(depositAmt)
                elif userChoice is 3:
                    savings.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()