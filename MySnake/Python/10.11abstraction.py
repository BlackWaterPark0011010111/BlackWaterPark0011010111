# class Animal:
#     def reproduce(self):
#         pass

# class Whale(Animal):
#     def reproduce(self):
#         print('The whale was created')
    


# class Mosquito(Animal):
#     def reproduce(sel):
#         print('This is a Mosquito object created today')


# whale1 = Whale()
# whale1.reproduce()
# animal1 = Animal()
# animal1.reproduce()

# mos = Mosquito()
# mos.reproduceMosquito()

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def reproduce(self):
#         pass
# class Whale(Animal):
#     pass


# animal = Animal()
# animal.reproduce()





from abc import ABC, abstractmethod


class AppleDeviceInterface(ABC):
    @abstractmethod

    def generateID(self):
        pass


    @abstractmethod
    def returnSignalFromMainBus(self):

        pass


class MetaverseGlasses():
    def generateID(self):

        return'ID: 126515132153'
    
    def returnSignalFromMainBus(self):
        return'0x6565151'
    
    
glasses = MetaverseGlasses()
print(glasses.generateID())
print(glasses.returnSignalFromMainBus())


class MRGlasses(AppleDeviceInterface):
    def generateID(self):
        return super().generateID()
    

    def returnSignalFromMainBus(self):
        return super().returnSignalFromMainBus()
    
    
    
mr = MRGlasses()
print(mr.generateID())
mr.returnSignalFromMainBus()