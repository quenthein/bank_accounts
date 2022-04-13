'''Déclaration des classes de comptes'''

#classe global de compte bancaire
class BankAccount:
    def __init__(self, account_number, owner_name, bank_balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.bank_balance = bank_balance

#definition de la méthode retrait
    def withdrawal(self, amount):
        if amount < 0:
            print("Withdrawn amount is negative.")
        if amount > self.bank_balance:
            print('Dont have sufficient balance, be careful of agios')
        self.bank_balance -= amount

#définition de la méthode versement
    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount is negative.")
        self.bank_balance += amount

#définition de l'affichage du solde
    def show_bank_balance(self):
        return self.bank_balance

#classe fille (compte courant) de compte bancaire
class CurrentAccount(BankAccount):
    def __init__(self, account_number, bank_balance, owner_name, overdraft, agios_percentage):
        super().__init__(account_number, owner_name, bank_balance)
        self.overdraft = overdraft
        self.agios_percentage = agios_percentage
        solde = float(self.show_bank_balance())
        if solde < self.overdraft:
            self.apply_agios()

# définition de la méthode d'application d'agios
    def apply_agios(self):
        print('%{} deducted for not maintaining sufficient balance'.format(self.agios_percentage))
        self.bank_balance *= (1 + self.agios_percentage)

# définition de retrait avec découvert => application d'agios
    def money_withdrawal(self, amount):
        super().withdrawal(amount)
        if self.overdraft:
            self.apply_agios()

# retour de l'affichage en string formaté à 0.2d
    def __str__(self):
        return 'Your Current account balance is now €{}'.format(round(self.show_bank_balance(), 2))

# définition de la classe fille (compte épargne) de compte bancaire
class SavingsAccount(BankAccount):
    def __init__(self, account_number, bank_balance, interest_percentage):
        super().__init__(account_number, bank_balance, interest_percentage)
        self.interest_percentage = interest_percentage

# définition de la méthode d'ajout d'intéret à chaque versement
    def addInterest(self):
        interest = self.show_bank_balance() * (self.interest_percentage / 100)
        self.deposit(interest)

    def money_withdrawal(self, amount):
        if amount < 0:
            print('Not possible to withdrawn this amount')
        pass

    def __str__(self):
        return 'Your Savings account balance is now €{}'.format(round(self.show_bank_balance(), 2))