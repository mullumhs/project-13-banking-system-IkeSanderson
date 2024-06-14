""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account
class BankManager:
    def __init__(self):
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

    def deposite(self, account, amount):
        for accounts in self.accounts:
            if accounts.get_number() == account:
                account.deposite(amount)
            else:
                print("Account Not Found")
    
    def withdraw(self, account, amount):
        for accounts in self.accounts:
            if accounts.get_number() == account:
                try:
                    account.withdraw(amount)

                except:
                    print("Balance Too Low")
            else:
                print("Account Not Found")


    def search_account(self, account):
        for accounts in self.accounts:
            if accounts.get_number() == account:
                print(account)
            
a1 = Account(1234,"John", 100)
bank = BankManager()

bank.add_account(a1)
bank.search_account(1234)
bank.deposite(1234, 100) # <---- Error 
bank.search_account(1234)
bank.withdraw(1234, 500)
bank.search_account(1234)