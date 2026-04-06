
  #function
def firstFunction():
    print("This is my first function")
    print('its doesnt not do anything')
    print('but it demonstrates how to avoid repetion of print function')
    

firstFunction()
funcTest = firstFunction()
print(funcTest)
print(type(funcTest))


def power(x,y):
      z = x**y
      return z
result = power(2.45, 3)
print( result)
print(type(result))

arg1 = input('Please specify the value you want to take to the power..')
arg2 = input('Please specify the value of x to which we willraise')
arg1 = float(arg1)
arg2 = float(arg2)
result = power(int(arg1), int(arg2))
print(result)
def add_number(num1, num2):
     sum = num1 + num2
     print('Sum: ', sum)
     

add_number(arg1, arg2)


 