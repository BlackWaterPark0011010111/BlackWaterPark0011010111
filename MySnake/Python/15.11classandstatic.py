class Bank:
    bank_name = 'Virtual Bame'

    def __init__(self, location) -> None:
        self.location = location

    def display_branch_location(self):
        print(f'The location of the{self.bank_name} branch is:  {self.location}')


    @classmethod
    def change_name(cls, new_name):

        cls.bank_name = new_name

    @staticmethod
    def greet_costomers(text_to_display):
        print( text_to_display)

bank1 = Bank('Germany')

bank2 = Bank('Poland')

bank3 = Bank('USA')

print(bank1.bank_name)
bank1.display_branch_location()
bank1.greet_costomers('Welcome to our new branch')
bank1.change_name('New Crypto Bank')


bank1.display_branch_location()
bank2.display_branch_location()
bank3.display_branch_location()
