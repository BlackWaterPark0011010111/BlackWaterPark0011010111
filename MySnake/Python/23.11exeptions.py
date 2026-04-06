try:
    with open('nonexistent.txt', 'r+') as f:
        f.read()
except FileNotFoundError:
    print('Im sorry but i could not find the file')

try:

    list1 = ['First','Second','Third','Fourth']
    print(list1[10])
except IndexError:
    print('The list1 is shorter: Index out of bounds error...')


try:
    x = 10
    y = 0
    print(x/y)
except(ZeroDivisionError):
    print('Sorry but u r trying to division on 0')



try:
    dict1 = {'key1':12, 'key2': 13}
    print(dict1['key3'])
except KeyError:
    print('There is no such entry in dict1. check exception.py line28')