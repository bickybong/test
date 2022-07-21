class Library:
    def __init__(self,books):
        self.availableBooks =books
    
    def display(self):
        print()
        print("Avaulable books: ")
        for book in self.availableBooks:
            print(book)

    def lend(self, request):
        if request in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(request)
        else:
            print("Sorry, book is not available in list")

    def addbook(self, returns):
        self.availableBooks.append(returns)
        print("You have returned the book. Thank you!")

class Customer:
    def request(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of a book you would like to return: ")
        self.book = input()
        return self.book

library = Library(["Yes", "No", "523"])
customer = Customer()

while True:
    print("Enter 1 to display available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.display()
    elif userChoice is 2:
        request = customer.request()
        library.lend(request)
    elif userChoice is 3:
        returnBook = customer.returnBook()
        library.addbook(returnBook)
    else:
        quit()