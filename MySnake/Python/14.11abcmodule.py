from abc import ABC, abstractmethod
#parent class
class BankAccount(ABC):
    def __init__(self, name,balance, accountNum):
        self.accountNumber=accountNum
        self.balance=balance
        self.accountHolderName=name
       
     
    @abstractmethod
    def deposit(self, amount):
        self.balance +=amount
        return f'new balance is {self.balance}'
    
    @abstractmethod
    def withdraw(self,amount):
        pass
    
    @abstractmethod
    def account_type(self):
        pass 
    
# child classes 
class SavingAccount(BankAccount):
    def __init__(self,name,balance, accountNum, interestRate):
       super().__init__(name,balance, accountNum) 
       self.interestRate=interestRate
         
    def deposit(self, amount):
        return super().deposit(amount)
    def withdraw(self,amount):
        pass
    
    def account_type(self):
        return 'Savings Account' 
           
    def add_interest(self):
        pass
class CheckingAccount(BankAccount):
    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self,amount):
        pass
    
    def account_type(self):
        return 'Checking  Account' 
           
class BusinessAccount(BankAccount):
    def __init__(self,name,balance, accountNum,interestRate):
        super().__init__(name,balance, accountNum)
        self.interestRate=interestRate
        
    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self,amount):
        pass
    
    def account_type(self):
        # return 'business account'
        return self.__class__.__name__
       
        
# savings 
my_savings=SavingAccount('jeremiah', 500, 12345, 2)
print(my_savings.balance)
# checkinng
my_checking_account= CheckingAccount('Jeremiah', 50, 12345)
print(my_checking_account.deposit(85))
# business
my_business = BusinessAccount('Mr Brown', 20000, 123456, 9)   
print(my_business.account_type())
# myAccount= BankAccount('Jeremiah', 1, 1234566)
# print(myAccount)