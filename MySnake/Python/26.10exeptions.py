newlist = [x for x in range(0,100,10)]
print(newlist)
print('---------------------------------------------------------')
for x in newlist:
    print(x)
    print('---------------------------------------------------------')
try:
    itr = iter(newlist)
    print(itr)
    #print(list(itr))
    print(next(itr))#0
    print(next(itr))#10
    print(next(itr))#20
    print(next(itr))#30
    print(next(itr))#40
    print(next(itr))#50
    print(next(itr))#60
    print(next(itr))#70
    print(next(itr))#80
    print(next(itr))#90
except StopIteration:
    print('Stop iteration exeption occured')