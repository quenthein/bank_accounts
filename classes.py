class BankAccount :
    '''This is the global bank account class'''
    def __init__(self, account_number, owner_name, bank_balance):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__bank_balance = bank_balance

    '''Method instance'''
    def