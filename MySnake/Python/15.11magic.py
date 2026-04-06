#TASK: create a class that returns each time a single instance of itself
#The normal class returns as many instances as there calls (instantiations)
#Abstract classes do not return anything
#In order to return a single instance each time we instantiate use singleton pattern
#Singleton pattern requires the usage of class variables to store one, single instance

class Student:
    role = "Teacher"
    def __init__(self, name):
        self.name = name

    def __new__(cls, name):# cls шо это
        print("Invoked __new__method...")
        return super().__new__(cls) #шо это бля такое???
        #pass 


#Consumers of Student class
s1 = Student("Paul")
s2 = Student("Anna")
s3 = Student("Ammar")
print('--------------------')
print(id(s1))
print(id(s2))
print(id(s3))

print(s1.name, s1.role)
print(s2.name, s2.role)
print(s3.name, s3.role)

#Changing role instance variable via an object instance
s1.role = "Student"

print(s1.name, s1.role)
print(s2.name, s2.role)
print(s3.name, s3.role)

#Class variables
Student.role = "Students"

#Instance vs class variables
print(s1.name, s1.role)
print(s2.name, s2.role)
print(s3.name, s3.role)


class A(object): 
    #override of __new__ magic method
    def __new__(cls): 
         print("Step 1. Creating instance") 
         return super().__new__(cls) 
  
    def __init__(self): 
        print("Step 2. Init is called") 

    def __str__(self):
        return "This is an object of class A."
    
    def __hash__(self) -> int:
        return 120300333333

obj = A()
#print(obj.__str__())
#print(obj.__hash__())
print(id(obj))

# print(A())
