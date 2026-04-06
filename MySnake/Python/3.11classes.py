class PersonalData:
    def __init__(self, name,surname,country):
        self.name = name
        self.country = country
        self.surname = surname

    def printPersonalData(self):
        print(f'personal data: {self.name} {self.country}{self.surname}')
                  
    def ThirdFunk(self):
        print('nothing')

x =PersonalData("Me","myself","i")
x.printPersonalData()



class SensitiveData(PersonalData):
    def __init__(self, name,surname,country,geneticCode):
        self.name = name
        self.country = country
        self.surname = surname
        self.geneticCode = geneticCode   

    
    def printSensitiveData(self):
        print(f'personal data: {self.name} {self.country}{self.surname}{self.geneticCode}')
        super().ThirdFunk()
    

personal1 = SensitiveData('paul','Polanski','Poland','X')
personal1.printPersonalData()
personal1.printSensitiveData()



class GrandParent:
    def print(self):
        print('I am a grandparent')

class ParentA(GrandParent):
    def print(self):
        print('I am a parent A')

class ParentB(GrandParent):
    def print(self):
        print('I am a parentB')

class Child(ParentA,ParentB):
    pass

child = Child()
child.print()

print(Child.mro())

print(child)