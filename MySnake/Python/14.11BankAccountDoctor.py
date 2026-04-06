from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, name, balance,accountNum ):
        self.accountNumber = accountNum
        self.balance = balance
        self.accountHolderName = name
        
    
    @abstractmethod# и staticmethod шо делает
    def deposit(self, total_amount):#декоратор здесь,что мы делаем?
        if total_amount < self.balance:
            self.balance -=total_amount   
            print(f'your {self.__class__.__name__} now contains {self.balance}')
            return total_amount
        return 'there are not enough funds in your account' # почкму через функции
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def account_type(self):
        pass



#child classes
class SavingAccount(BankAccount):
    def __init__(self, name, balance, accountNum, interestRate):#почему тут так записано
        super().__init__(name, balance, accountNum)#и тут так записано
        self.interestRates = interestRate


    #####почему этот туту стоит
    def deposit(self, amount):# почкму через функции
        interest = self.addInterest(amount)
        print(f'you are depositing {amount}.\nyour added interest is {{interest}}')
        return super().deposit(amount + interest)

    def withdraw(self,amount):
         return super().withdraw(amount)
    def account_type(self):
        return super().__class__.__name__


    def addInterest(self,amount):
        return (amount/100)*self.interestRates





class CheckingAccount(BankAccount):
    def deposit(self, amount):# почкму через функции
        return super().deposit(amount)
    def withdraw(self,amount):
            pass
    def account_type(self):
            return 'savings Account'

    def addInterest(self):
            pass



class BussinessAccount(BankAccount):
    def __init__(self,name ,balance, accountNum ,interestRate):
        super().__init__(name,balance,accountNum)
        self.interestRate = interestRate

    def deposit(self, amount): # почкму через функции
        return super().deposit(amount)
    def withdraw(self,amount):
            pass
    def account_type(self):
            return self.__class__.__name__

        
my_savings = SavingAccount('Jerry', 500, 12345,2)
print(my_savings.balance)

my_checking_account = CheckingAccount('jerry', 50,1234)
print(my_checking_account.balance)

my_business = BussinessAccount('mr.Brown', 2000, 12354, 9)
print(my_business.account_type())
#myaccount = BankAccount('Jerry', 1, 123456)
#print(myaccount)



my_savings=SavingAccount('jeremiah', 5000, 12345, 2.5)

while True: 
    print('1) view balance')
    print('2) deposit money  ')
    print('3) withdraw money')
    print('4) Return Card')
    
    choice = int(input('please select your option (1-4): '))   
        
    match choice: 
        case 1:
            print(my_savings.balance)
        case 2:
            amount= float(input('how much would you like to deposit?:'))
            print(my_savings.deposit(amount))
        case 3: #withdraw
            amount =float(input('how much would you like to withdraw?:'))
            print(my_savings.withdraw(amount))
        case 4:
            print('returning card')
            exit()
        case _:
            print('please select a number between 1-4')