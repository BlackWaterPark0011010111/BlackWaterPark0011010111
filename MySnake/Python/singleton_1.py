#class Singleton:
#    instance = None
#
#    def __new__(cls):
#        if Singleton.instance is None:
#            Singleton.instance = super().__new__(cls)
#        return Singleton.instance
#    
#if __name__=="__main__":
#    first = Singleton()
#    print(first)
#    second = Singleton()
#    print(second)
#    print(first is second)        
#



#class Singleton(object):
#    __instance = None
#
#    def __new__(cls, *args, **kwargs):
#        if cls.__instance is None:
#            cls.__instance= super(Singleton, cls).__new__(cls, *args, **kwargs)
#            return cls.__instance
#        
#singleton = Singleton()
#singleton_two = Singleton()
#print(singleton is singleton_two)
            


class Singleton(type):

    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]

#
    
class DatabaseConnection(metaclass=Singleton):
    pass


class SingletonExample(metaclass=Singleton):
    pass

connectio = DatabaseConnection()
connectio2 = DatabaseConnection()

print(connectio is connectio2)

object1 = SingletonExample()
object2= SingletonExample()

print(object1 is object2)