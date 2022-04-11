from constantes import *
print(interest_percentage)

class BankAccount:
    '''This is the global bank account class'''
    def __init__(self, account_number, owner_name, bank_balance):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__bank_balance = bank_balance


class CurrentAccount(BankAccount):
    '''This is the current bank account child class'''
    def __init__(self, overdraft, agios_percentage):
        BankAccount.__init__(self, owner_name)
        self.overdraft = overdraft
        self.agios_percentage = agios_percentage


class SavingsAccount(BankAccount):
    '''This is the SavingsAccount bank account child class'''
    def __init__(self, interest_percentage):
        BankAccount.__init__(self, owner_name)
        self.interest_percentage = interest_percentage

