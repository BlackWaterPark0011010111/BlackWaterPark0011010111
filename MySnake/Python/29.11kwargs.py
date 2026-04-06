# def myfunc(**kwargs):
#     print(kwargs)
#     print(kwargs["name"])
#     print(kwargs["age"])
#     try:
#         print(kwargs["nonexistent"])
#     except KeyError:
#         print("This key does not exist. Try again...")
 
 
# #One way of calling a function that expects **kwargs
# myfunc(name="Paul", age=2, bank="My Bank")
 
 
# #Passing a dict from a calling code
# dict = {"name":"Paul", "age":2, "bank":"My Bank"}
# try:
#     print(dict) 
#     myfunc(dict)
# except TypeError:
#     print("Passing a dict using dict unpacking")
#     myfunc(**dict)
 
 
# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result
 
# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
 
# dict2 = {"a":"Real", "b":"Python", "c":"Is", "d":"Great", "e":"!"}
 
# dict3 = {"f":"Real", "g":"Python", "h":"Is", "i":"Powerful", "e":"but Slow!"}
 
# #1. Use case of **operator outside of the function definition (unpacking)
# combined = {**dict2, **dict3}
# #combined2 = {dict2, dict3}
 
# print(combined)
# #print(combined2)
 
 
class A():
 
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        self.preferences = kwargs
 
    def show(self):
        for x, y in self.preferences.items():
            print(f"The value of {x} is {y}!")
 
 
 
a = A(4, 5, name="Paul", bank="Any Bank")
a.show()
print(a.__dict__)
b = A(3, 5,  surname="Polanski", country="Spain", city="Alicante")
b.show()
print(b.__dict__)
c = A(2, 5, brand="Apple", version=13, os="iOS", color="dark green")
c.show()
print(c.__dict__)
 
 
#TASK 1
#Flexible class
#
#1. Create a class A that will use a flexible constructor that accept any key-value pair duing
#object initialization (hint: use **kwargs)
#2. Then, create a show() method that will print all the values of an object 
#3. Create 3 objects a, b and c with 3, 4 and 5 different key-value pairs and display values