x = 10
y = 'My string'
z = [1,2,3,4,5,7]
d = {'key1' : 1,'key2' : 56}

class A(object):
    secret:12

    def __init__(self, graduated):
        self.graduated = graduated


    def __len__(self):
        return 111

    def __str__(self):
       # super().__str__()
        return f'The object class A has been created : {self.graduated}'


    def __eq__(self, another):
        #return id(self) == id(another)
        return self.graduated ==another.graduated
a = A(2020)
b = A(2021)
c = A(181541)
d = A(1234)


print(a == b)
print(a == c)
print(b == c)

#print(len(x))

print(len(y))
#print(len(b))
print(len(z))
print(type(len(d)))

print(str(a))
print(a)
print(b)
print(c)