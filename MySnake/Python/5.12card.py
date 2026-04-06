class Book:
    def __init__(self,title,quantity,author,price) -> None:
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price
    

    def __repr__(self) -> str:
        return f'Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: ${self.get_price()}'


book1 = Book('Python Crash Cource', 2, 'Eric Maths', 35)
bulkBooks = Book('Python Crash Course', 48, 'Eric Maths', 35)
bulkBooks.set_discount(0.20)
print(book1.get_price())
print(bulkBooks.get_price())
print(book1)


class Novel(Book):
    def __init__(self, title, quantity, author, price, branch) -> None:
        super().__init__(title, quantity, author, price)