# 1. Liberal implementation of abstraction pillar using traditional Python coding
class Animal:
    def reproduce(self):
        raise NotImplementedError("Animal reproduce method should be implemented")

class Whale(Animal):
    def reproduce(self):
        print("The whale was created...")

class Mosquito(Animal):
    def reproduce(self):
        print("This is a Mosquito object created today...")

whale1 = Whale()
whale1.reproduce()
# animal = Animal() #Animal can be instantiated
# animal.reproduce()
mos = Mosquito()
mos.reproduce() #No forced implementation of the reproduce method


# Forced implementation of methods defined in the Parent class
from abc import ABC, abstractmethod
from typing import Protocol

# class Animal(ABC): #It is an abstract class. Has to be inherited from.
#     @abstractmethod
#     def reproduce(self):
#         pass

# class Whale(Animal):
#     pass


# # animal = Animal() #Expected: Exception has occurred: TypeError. Can't instantiate abstract class Animal with abstract method reproduce
# # animal.reproduce()

# whale1 = Whale() #Expected error: Exception has occurred: TypeError....
# whale1.reproduce()

from abc import ABC, abstractmethod

class AppleDeviceInterface(ABC):
    @abstractmethod
    def generateID(self):
        return "Default implemention of device ID: XXX-123-XXXXX"
    
    @abstractmethod
    def returnSignalFromMainBus(self):
        pass

    @property
    @abstractmethod
    def registerWithAICloud(self):
        pass

# Imagine the following scenario:
# You are another company that wants to communicate with the producer of HardwareProducer
# Your engineers developed new metaverse Mixed Reality glasses and you want integrate with Apple products

# 1st class implementing abstract class (interafce)
class MetaverseGlasses(AppleDeviceInterface):
    def __init__(self, cloud_id) -> None:
        self.__cloud_id = cloud_id

    #implement method1
    def generateID(self):
        return "ID:122994444"
    
    #implement method2
    def returnSignalFromMainBus(self):
        return "0x3493c99333c"
    
    #implement new method from Apple
    @property
    def registerWithAICloud(self):
        return self.__cloud_id
    
    @registerWithAICloud.setter
    def registerWithAICloud(self, value):
        self.__cloud_id = value
    
glasses = MetaverseGlasses(123000)
print(glasses.generateID())
print(glasses.returnSignalFromMainBus())
print(glasses.registerWithAICloud)
glasses.registerWithAICloud = 99939393
print(glasses.registerWithAICloud)

#2nd class implementing abstract class (interafce)
class MRGlasses(AppleDeviceInterface):
    def generateID(self):
        return super().generateID()
    
    def returnSignalFromMainBus(self):
        return super().returnSignalFromMainBus()
    
    def registerWithAICloud(self):
        return super().registerWithAICloud()
    
mr = MRGlasses()
print(mr.generateID())
mr.returnSignalFromMainBus()

#3rd approach to Abstraction using Protocols (between traditional Python and ABC)

class Loggable(Protocol):

    def log(self, message:str) -> None:
        pass

class VRLogger():

    def log(self, message:str) -> None:
        print(f"The message from the VR Logger is: {message}.")

class ARLogger:

    def log(self, message:str) -> None:
        print(f"The Augmented Reality logger: {message}.")

class MRLogger:
    
    def logNonConform(self, whatever:str):
        pass

def printLogs(logs:Loggable) ->None:
    print(f"LOG: {logs}")
    print(f"Message logs: {logs}")

vr = VRLogger()
vr.log("Virtual Reality Headset nr 1 started at 14:49.")

ar = ARLogger()
ar.log("Augmented Reality Headset is ready.")

mr = MRLogger()
mr.logNonConform("This is a non-conforming Logger...")
printLogs(vr)
printLogs(ar)
printLogs(mr)

#prot = Loggable() #Expected error: Protocols cannot be instantiated






