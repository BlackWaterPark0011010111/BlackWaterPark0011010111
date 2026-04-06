"""Exercise: Library Management System

# Backstory:
You've been hired to develop a library management system for a local library. The library wants to modernize its operations and improve user experience. You'll be creating a Python program that simulates the library's functionalities.

# Objectives:
Design and implement a Library class to manage books, patrons, and transactions. The program should provide options to borrow and return books, check available books, and more.

# Tasks (Sugestions):

1) Create a Book Class:
- Design a Book class that contains information about a book, such as its 
    >title, 
    >author, 
    >Reference Number,
    >availability status.

2) Create a Patron Class:
- Design a Patron class that represents library patrons. 
- Patrons should have attributes like 
    >name, 
    >email
    >library card number, 
    > and a list of borrowed books.

3) Create a Library Class:
- Implement a Library class that manages books, patrons, and transactions.

4) The Library class should have methods for:
- Adding books to the library.
- Registering new patrons.
- Borrowing books (a patron checks out a book).
- Returning books (a patron returns a book).
- Checking the availability of a book.
- Displaying a list of all books in the library.
- Displaying a list of all registered patrons.
- Displaying a list of all transactions (who borrowed which book and when).

5) User Interface:
- Implement a command-line user interface that allows library staff to interact with the system.
- Provide options to perform the actions mentioned above, and guide the user through the process.

6) Resource Tracking:
Ensure that the Library class keeps track of available books and who has borrowed them.

7) Transaction History:
Record transaction history, so it's possible to view who borrowed or returned a book and when.

# Error Handling: *Good Practice*
Implement error handling to handle scenarios like a patron trying to borrow an unavailable book, returning a book they didn't borrow, or entering invalid book titles or patron card numbers.

# Additional Tips: *Senior*
- Create well-structured classes with clear separation of responsibilities.
- Use appropriate data structures to manage books, patrons, and transactions.
- Consider how to handle edge cases and provide informative error messages when needed.
- Make the user interface intuitive and user-friendly.

# Summary:
This exercise simulates the development of a library management system. It's a practical application of object-oriented programming principles, including class design, methods, data structures, and user interaction. You'll gain experience in building a system that manages resources, tracks transactions, and provides functionality to library staff.
"""

import random
from datetime import datetime
class Book:
    MAXIMUM_AVAILABLE_BOOKS = 0
    def __init__(self, title: str, author: str, number: int = 100):
        self.title = title
        self.author = author
        self.reference_number = Book.generate_ref_number()
        self.number = Book.handle_book_number(number)
        self.MAXIMUM_AVAILABLE_BOOKS = Book.handle_book_number(number)
    
    def handle_book_number(number):
        number = str(number)
        if number.isdigit():
            return int(number)
        else:
            raise ValueError("Invalid Number")

    def availability(self) -> bool:
        return self.number > 0
    
    def borrow_me_out(self):
        if self.availability(): 
            self.number -= 1
        else:
            raise ValueError("Book is not available for borrowing")
    
    def return_me_back(self):
        if self.number < self.MAXIMUM_AVAILABLE_BOOKS:
            self.number += 1
        else:
            raise ValueError("You cant add more books than available")
    
    def supply_more_books(self, amount):
        self.number += amount
        self.MAXIMUM_AVAILABLE_BOOKS += amount

    @staticmethod
    def generate_ref_number() -> str:
        return "".join(random.choice(["a","b","c","d"]) for i in range(5))
    
    def __str__(self):
        return self.title

# Human class,  then Patron (inheriting from Human)
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    

class Patron(Human):
    def __init__(self, name: str, age: int, email: str):
        super().__init__(name, age)
        self.email = email
        self.library_card_number = Patron.generate_library_number()
        self.borrowed_books = []
    

    @staticmethod
    def generate_library_number() -> str:
        res =  "".join(random.choice(["a","b","c","d"]) for i in range(5))
        return f"LIB_ID_{res}"
    
    def borrow_book(self, book: Book):
        if isinstance(book, Book) and book.availability():
            self.borrowed_books.append(book)
        else:
            print("I couldnt recognise that book")
    
    def __str__(self):
        return self.name

class Transaction:
    def __init__(self):
        self.ledger = {}
    
    def record_book_borrow(self, book, patron):

        self.ledger[f"{patron}-{str(datetime.today())}"] = f"{book},{patron},{str(datetime.today())}"
    
    def record_book_return(self, book, patron):
        self.ledger.pop(f"{patron}-{str(datetime.today())}")
    

class Library:
    def __init__(self):
        self.books = {} # we will also want to search for a book
        self.patrons = {}
        self.transactions = Transaction() # composition

    def add_book_to_shelf(self, title: str, author: str, number = 100):
        book = Book(title, author, number) # composition
        print(f"Adding book {book} to my library")
        if not self.books.get(f"{str(book)}"):
            self.books[f"{str(book)}"] = book
    
    def register_patron(self, name: str, age: int, email: str):
        new_patron = Patron(name, age, email) # composition
        if not self.patrons.get(f"{str(new_patron)}"):
            self.patrons[f"{str(new_patron)}"] = new_patron
    
    def borrow_a_book(self, book: Book, patron):
        if book.availability():
            print(f'Book {book} is availible for Borrowing')
            book.borrow_me_out()
            print(f'Book {book} has been borrowed')
            self.transactions.record_book_borrow(book, patron)
            print(f'Book{book} borrowed has been recorded')
    
    def return_a_book(self, book: Book, patron):
        book.return_me_back()
        self.transactions.record_book_return(book, patron)
        print(f'Book: {book} has been returned ')
    
    def check_availability_of_book(self, book: Book):
        if self.books.get(f"{str(book)}") and book.availability():
            return f"{str(book)} is Available"
        else:
            return f"{str(book)} is not Available"
    
    def display_books(self):
        print("Displaying all books in this library")
        for book in self.books:
            print(book)
    
    def display_patrons(self):
        for patron in self.patrons:
            print(patron)
    
    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)


    
options = {
    "1": "Add book to the Library",
    "2": "Register New Patron",
    "3": "Borrowing a book",
    "4": "Returna book to the Library",
    "5": "Check for a book",
    "6": "display all library information",
    "7": "quit",
}

chosen_option = True
while chosen_option:
    prompt = f"please select an action .\n{options}"
    response = input(prompt)
    if not options.get(response):
        print("invalid_option")
    else:
        library = Library()
        if response == "1":
            book_title = input("Title of the book: ")
            book_author = input("Author of the book: ")
            number = input("Number of the books to supply: ")
            library.add_book_to_shelf(book_title, book_author, number)
            library.display_books()
        elif response == "2":
            patron_name = input('what is the name of the Patron: ')
            patron_email = input('Whats ure email')
            patron_age = input('Whats ure age: ')#
            library.register_patron(patron_name,patron_age,patron_email)
            library.display_patrons()
            library.borrow_a_book()
        elif response =="3":
            library.add_book_to_shelf('test book', 'test author', 34)
            library.register_patron('test patron', 55, 'test@test.com')
            my_book = library.books.getattr('test book')
            patron = library.patrons.getattr('test patron')
            #print(my_book, patron)
            library.display_books()
            library.borrow_a_book(my_book, patron)
            library.display_books()
            library.return_a_book(my_book, patron)
            library.display_books()