#from math import*

class MyownType:
    name = 'Paul'
    surname = 'Polanski'
    favourites = ['guitars', 'coffee']
   
object = MyownType()
object2 = MyownType()
print(object.favourites[0])

print(object.favourites[0])



print('--------------------------------------------------------1---')
########2й вариант вывода ООП и класса MyownType---->

class Employee:
   
    def __init__(self, name,surname, employmentYear):
        self.name = name
        self.surname = surname
        self.employmentYear = employmentYear
       

    def __str__(self):
        return f'{self.name} {self.surname} {self.employmentYear}of type MyownTupe'

    def yearsOfwork(self,employmentYear):
        return 2023 - self.employmentYear

emp1 = Employee('Paul', 'Polanski', 2020)


print(emp1)


print('--------------------------------------------------3йвариант---')
from dataclasses import dataclass

@dataclass

class MyownDataClass:
    name: str
    surname: str
    year: int

obj = MyownDataClass('Paul', 'Polanski', 2020)
print(f'{obj.name} {obj.surname} {obj.year}')






# AB = float(input('Lenght first katet: '))
# AC = float(input('Lenght second katet: '))

# BC = sqrt(AB ** 2 + AC ** 2)
# S = (AB*AC) / 2
# P = AB+ AC + BC
# print('Square is: ', S)
# print('Perimeter is: ', P)