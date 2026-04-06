a = 5
isinstance(a, int)
isinstance(a, float)

b = True
isinstance(b, bool)
isinstance(b, int)
type(b) == int
print(b)


data = (4.5, 8.7, True, 'книга', 6, 8, 10, [True, False])

s = 0

for x in data:
    if isinstance(x, float):
        s +=x

print(s)


a = sum(filter(lambda x: isinstance(x, int), data))

print(a)




def defining(f):
    if isinstance(f, Circle):
        return 'this is a circle'
    elif isinstance(f, Trial):
        return 'this is a trial'
    elif isinstance(f, Squer):
        return 'This is a square'
    else:
        return 'Unknown'

    
class Circle:
    pass
 
class Trial:
    pass

class Squer:
    pass

C = Circle()
T = Trial()
S = Squer()

print(defining(C))
print(defining(T))
print(defining(S))
    

def get(x):
    res = None if x < 0 else x** 0.5
    return res
    return x

a = get(49)
print(a)

def getmax(a,b):
    return a if a > b else b


PERIMETR = False
if PERIMETR:
    def getrect(a,b):
        return 2 *(a+b)
else:
    def getrect(a,b):
        return a * b

print(getrect(1.5, 3.8))
x,y = 5, 7
print(getmax(x, y))



def even(x):
    return x%2 ==0

for i in range(1,20):
    if even(i):
        print(i)









def get_V(a,b,c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a * b * c


V = get_V(6 ,1,3)
print(V)





def add(value, lst = None):
    if lst is None:
        lst = []

    lst.append(value)

    return lst
l = add(1)
l = add(2, l)

print(l)