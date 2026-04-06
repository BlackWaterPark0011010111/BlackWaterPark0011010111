from enum import Enum
import datetime

class Weekday(Enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

myDay = Weekday.SUNDAY
print(myDay.name)
print(myDay.value)
weekday = datetime.datetime.now().isoweekday()
for day in Weekday:
        if day.value == weekday:
                print(f'----u r here, todays {day.name.lower()}')
        if day.value <5:
                print('we have to go to work')
        else:
                print('its time to get rest a lil bit')


class InterfaceOptional(Enum):
        BARRISTA = 1
        CAFFEELATTE = 2
        CAPPUCCINO = 3
        START = 4
        FINISH = 5

barrista = InterfaceOptional.BARRISTA
baristName = barrista.name
baristavalue = barrista.value
print(f'Barrista name: {baristName} and Barrista value: {baristavalue}')
#useroption = int(input('Please enter your option(type 1-5): '))


#if useroption ==barrista.value:
 #       print(f'You selected {baristName} coffee')



class Person:
        def __init__(self, name, age):
                self.name = name
                self.age = age
        def __str__(self):
                return f'{self.name}   {self.age}'
        
p1 = Person('John', 36)
print(p1)