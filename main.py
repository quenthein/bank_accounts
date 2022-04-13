'''interface en ligne de commande'''
#import des classes
from comptes import *

#constantes pour l'interface
CURRENT_ACCOUNT = '1'
SAVINGS_ACCOUNT = '2'
BALANCE = '1'
WITHDRAWN = '2'
DEPOSIT = '3'
EXIT = '4'

YES = 'y'
NO = 'n'


# définition du choix de compte pour une dépense
def choose_account():
    choosing = None
    if choosing != CURRENT_ACCOUNT:
        print('''Which account do you want to modify ?
                1 - CURRENT ACCOUNT
                2 - SAVINGS ACCOUNT''')
        choosing = input()
    elif choosing != (SAVINGS_ACCOUNT):
        print('''Which account do you want to modify ?
                1 - CURRENT ACCOUNT
                2 - SAVINGS ACCOUNT''')
        choosing = input()
    if choosing == CURRENT_ACCOUNT:
        account = current
        print('How many do you want to withdrawn ?')
        amount = float(input())
        account.money_withdrawal(amount)
        print(current)
    elif choosing == SAVINGS_ACCOUNT:
        account = savings
        print('How many do you want to withdrawn ?')
        amount = float(input())
        account.money_withdrawal(amount)
        print(savings)

# dépot d'une somme
def deposit_money():
    choosing = None
    if choosing != CURRENT_ACCOUNT:
        print('''In which account do you want to deposit your amount ?
                   1 - CURRENT ACCOUNT
                   2 - SAVINGS ACCOUNT''')
        choosing = input()
    elif choosing != (SAVINGS_ACCOUNT):
        print('''In which amount do you want to deposit your amount ?
                   1 - CURRENT ACCOUNT
                   2 - SAVINGS ACCOUNT''')
        choosing = input()
    if choosing == CURRENT_ACCOUNT:
        account = current
        print('How many do you want to deposit ?')
        amount = float(input())
        account.deposit(amount)
        print(current)
    elif choosing == SAVINGS_ACCOUNT:
        account = savings
        print('How many do you want to deposit ?')
        amount = float(input())
        account.deposit(amount)
        print(savings)

# montrer le compte actualisé
def show_balance():
    savings.show_bank_balance()
    current.show_bank_balance()

# méthode de l'interface de départ proposant le choix des options
def started_interface():
    print('''Hello there !
    What do you want to do today ?
    1 - Check my balances
    2 - Withdraw an amount
    3 - Deposit an amount
    4 - Exit''')
    choice = input()
    if choice == BALANCE:
        show_balance()
        print(current)
        print(savings)
        print('Do you want to do something else (y : yes | n : no) ?')
        other_choice = input()
        if other_choice == 'y':
            started_interface()
        elif other_choice == 'n':
            print('See you soon')
        else :
            print('Please choose a number in the list')
            show_balance()
    elif choice == WITHDRAWN:
        choose_account()
        print('Do you want to do something else (y : yes | n : no) ?')
        other_choice = input()
        if other_choice == 'y':
            started_interface()
        elif other_choice == 'n':
            print('See you soon')
        else:
            print('Please choose a number in the list')
            choose_account()
    elif choice == DEPOSIT:
        deposit_money()
        print('Do you want to do something else (y : yes | n : no) ?')
        other_choice = input()
        if other_choice == 'y':
            started_interface()
        elif other_choice == 'n':
            print('See you soon')
        else:
            print('Please choose a number in the list')
            started_interface()
    elif choice == EXIT:
        print('See you soon')
    else:
        print('Please choose a number in the list')
        started_interface()

# déclaration des valeurs de tests
owner_name = 'toto'
account_number = '1234'
agios_percentage = 3.8
interest_percentage = 6
bank_balance = 400
overdraft = bank_balance

current = CurrentAccount(account_number, bank_balance, owner_name, overdraft, agios_percentage)
savings = SavingsAccount(account_number, bank_balance, interest_percentage)

started_interface()