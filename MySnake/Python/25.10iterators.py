# mystring = 'This is my string'#String is iterable because we can use a for loop
# for x in mystring:
#     print(x)

# iterator = iter(mystring)
# iterator2 = iter(mystring)
# print(iterator)#
# print(list(iterator2))# grab all values
# print(next(iterator))
# print(next(iterator))
# iterator3 = iter([2234, 222, 4334])#,1,2,3
# print(next(iterator3))#1
# print(next(iterator3))#2
# print(next(iterator3))#3





mylist = [12,2,45,1,75255,4,645745]
newlist = []
# for x in mylist:
#     newlist.append(x)
#     print(newlist)

newlist = [x*2 for x in mylist if x> 100000]
print(newlist)
newlist = {x*2 for x in mylist if x> 100000}# это так же работает с Set с фигурными скобками
print(newlist)


def mygenerator():
    
    yield 1
    yield 2
    yield 3

f = mygenerator()
print(f)
print(next(f))

# for x in f:
#     print(x)

