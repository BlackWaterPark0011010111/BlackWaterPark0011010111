import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will  get logger to a file')
logging.critical('This is a critical error')
logging.info('This is an info message')
logging.warning('This is an a warning')
logging.error('This is an error message')
logging.critical('this is a critical message')


class GreaterThanTenError:
    pass

class A:
    def abstract_function(self):
        raise NotImplementedError
    

a = A()
#a.abstract_function()


class B(A):
    def abstract_function(self):
        print(('B was called...'))

    def accept_value_below_ten(self, val):
        if val < 10:
            logging.warning('Congrats u may proceed further ')
        else:
            try:
                
                raise GreaterThanTenError('The value passed has to be 10 or greater')
            except:
                print('Lets see if it gets executed')
                logging.critical('Line 122 in exeptions.py file caused an error. greater than 10 value was passed. ')
                raise

b = B()
b.abstract_function()
b.accept_value_below_ten(9)


import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')