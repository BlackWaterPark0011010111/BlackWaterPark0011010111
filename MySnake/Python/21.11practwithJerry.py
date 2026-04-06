'''
for x in range(-5,6):
    if x !=0:
      print(x)
number = -5


while number <=5:
    print(number,'', end ='')
    number +=1
    if number ==0:
        number+=1
'''

text = 'huhdnfvisnjlv iuhrkshrfivu h  if hkhid huiuhdiuhf'
search = input('what should be found? ').strip()

index = 0


while index< len(text):
    found_index = text.find(search,index)

    if found_index == -1:
        break
    print(f"found '{search}' at index: {found_index} ")
    index= found_index +1


number1 = int(input('Enter a number from 1 to 100: '))
number2 = int(input('Enter a number from 1 to 100: '))
divisor = int(input('Enter a number from 1 to 100 to be the divisor: '))
range1 = range(number1,number2 + 1)

while range1:
    print('Starting: {}\nEnding: \nDivisor: {}\n'.format(number1, number2, divisor))
    for x in range1:
        if divisor ==0:
            pass
        elif x % divisor ==0:
          print('{} is divisible by {}'.format(x, divisor)) 
    break