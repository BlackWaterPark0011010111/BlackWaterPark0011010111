#OOP
#1.Abstraction Principle
#2.Inheritance Principle (e.g. multiple inheritance)
#3.Polymorphim Principle (e.g. method overriding in the inheritance chain)
#4.Encapsulation Principle (e.g. private vs public access modifiers)
     
from abc import ABC, abstractmethod
     
#Abstract class (interface in other languages)
class VehicleSpecification(ABC):
     
    @abstractmethod
    def start(self):
        pass
     
    @abstractmethod
    def stop(self):
        pass
     
     
#Conrete class
class Car(VehicleSpecification):
     
    def start(self):
        print("The car started to run...")
     
    def stop(self):
        print("The car has stopped....")
     
    def driving(self):
        print("The car is driving....")
     
#Conrete class
class Ship(VehicleSpecification):
     
    def start(self):
        print("The ship's engine has started...")
     
    def stop(self):
        print("The ship has stopped...")
     
    def sailing(self):
        print("The ship is sailing")
     
     
class SportCar(Car):
    
    def start(self):
        print("The sport car started the engine...")
     
    def driving(self):
        print("My sport car has just started to drive like crazy...")
     
car = Car()
car.start()
car.stop()
car.driving()
     
ship = Ship()
ship.start()
ship.stop()
ship.sailing()
     
sport = SportCar()
sport.start()
sport.stop()
sport.driving()
     


