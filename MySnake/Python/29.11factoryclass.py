class Vehicle():


    @staticmethod
    def factory(type):
        if type=="Car":
            return Car()
        if type =='Bike':
            return Bike()
        if type =='Airplane':
            return Airplane()
        if type =='Whale':
            return Whale()
        raise NotImplementedError

class Car:
    def start(self):
        print('The car is driving')

class Bike:
    def start(self):
        print('The bike is driving')

class Airplane:
    def start(self):
        print('The airplane is driving')

class Whale:
    def start(self):
        print('The whale is driving')

car = Vehicle.factory('Car')
car.start()

car2 = Car()
car2.start()
plane = Vehicle.factory('Airplane')
plane.start()
bike = Vehicle.factory('Bike')
bike.start()



