class Apple:
    manufacturer = "Apple Inc."
    website = "www.apple.com/contact"
    def contact(self):
        print(f"To contact us, log on to {self.website}")

class Macbook(Apple): #inherit from Apple its methods and attributes
    def __init__(self):
        self.yearManufactured = 2017
    
    def manufactureDetails(self):
        print(f"This macbook was manufactured in the year {self.yearManufactured} by {self.manufacturer}")

mac = Macbook()
mac.contact()
mac.manufactureDetails()
