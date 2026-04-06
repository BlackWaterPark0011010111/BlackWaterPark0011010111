#list_of_integers = []
#while True:
#    try:
#        number = float(input('Type a number:  '))
#        if number ==0:
#            break
#        list_of_integers.append(number)
#    except(ValueError):
#        print('INVALID INPUT: u r allowed to input only integers and floats')
#try:
#    print(f'The avrg is: ', round(sum(list_of_integers)/(len(list_of_integers)),2))
#except (ZeroDivisionError):
#    print('U r not allowed to enter 0 as first argument...')
#
#
#
#txt = """King Lear is a tragedy written by 
#William Shakespeare. It is based on the mythological
#Leir of Britain. King Lear, in preparation for his old age,
#divides his power and land between his daughters Goneril and
#Regan. The Kings third daughter, Cordelia, """
#
#print('Text: .\n', txt)
#n = 0
#to_find = input('What should be found?: ')
#while n< len(txt):
#    if to_find ==txt[n]:
#        print('Character ', to_find, 'found at index', n)
#
#    n+=1
#
#    #re-write using for loop(using in range)
#print(txt.find('King'))


c = 1
while c !=0:
    a  = int(input('Type of starting integer: '))
    b = int(input('Type of ending integer: '))
    #if a > b or b < a :
        #print(f'i am sorry but  the second value should be greater than the first one')
    c = int(input('Type of divisor:'))
    print('\n')


    while a < b and c != 0:
        if a%c ==0:
            print(a, 'is divisor by ', c)
        a +=1
    print( '\n')


   # catch the errors and handle them gently (try not ot terminate programm)
   # make sure that the second number is always greater than the first one(logical errors)
    #try re-wrighting