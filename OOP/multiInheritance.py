from xml.etree.ElementTree import TreeBuilder


class OS:
    multitasking = True
    name = "Iphone Os"

class Apple:
    website = "www.apple.com"
    name ="Apple"

class Macbook(OS, Apple): # 2 inheritance classes
    number = 89324890
    def __init__(self) -> None:
        if self.multitasking is True:
            print(f"This is a multi tasking system, visit {self.website} to learn more")
            print(f"Name = {self.name}")

class Iphone(Macbook):# 3rd level of inheritance
    def __init__(self) -> None:
        if self.multitasking is True:
            print(f"This is a multi tasking system, visit {self.website} to learn more")
            print(f"Name = {self.name}")
            print(f"number = {self.number}")

phone = Iphone()