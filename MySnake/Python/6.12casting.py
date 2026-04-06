x = 1
y = 1.2
z = x/y

print(z)
print(type(y))
print(type(z))
ss = int('12363534')
print(ss)
print(type(ss))

#ee = int('this is a string')

#print(ee)

try:
    x = list(1,2,3)
    y = 0
except:
     pass
try:
        z = x/y
except TypeError:
        print(f'The value of x is: {x} and type of x is {type(x)}')
except Exception:
        print('An error has occurred')





class MathematicalError(Exception):
    pass

def parse_input(user_input):
    try:
        elements = user_input.split()

        if len(elements) != 3:
            raise MathematicalError("Invalid input: must consist of three elements")

        n1 = float(elements[0])
        n2 = float(elements[2])

        op = elements[1]
        if op not in ['+', '-']:
            raise MathematicalError("Invalid operator: must be '+' or '-'")

        return n1, op, n2

    except ValueError:
        raise MathematicalError("Invalid input: unable to convert to float")

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2

while True:
    user_input = input('>>> ')
    
    if user_input.lower() == 'quit':
        break
    
    try:
        n1, op, n2 = parse_input(user_input)
        result = calculate(n1, op, n2)
        print(result)
    except MathematicalError as e:
        print(f"Error: {e}")