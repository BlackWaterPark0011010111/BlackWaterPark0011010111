class Animal:
    def make_noise(self):
        print("shh")

class Cat(Animal):
    def make_noise(self):
        print("meow")


class Dog(Animal):
    def make_noise(self):
        print("gavv")

def noise(animal: Animal):
    animal.make_noise()

if __name__ == "__main__":
    noise(Cat())