class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name= first_name
        self.last_name = last_name
        self.age = age

    def describe(self):
        print(f'I am {self.first_name} {self.last_name}. Im {self.age} years old')

if __name__=='__main__':
    Ivan = Person('Ivan','Ivanov', 20)

    Ivan.describe()