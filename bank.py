""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account
from transactions import Transaction
class BankManager:
    def __init__(self):
        self.accounts = []
        self.transactions = []
    
    def add_account(self, account):
        for accounts in self.accounts:
            if account.get_number == account:
                print("Account Already Exists")
                return False
        self.accounts.append(account)
        return True

    def deposit(self, account_num, amount):
        account = self.check_account(account_num)
        if account:
            account.deposit(amount)
            self.transaction_log(account_num, "Deposite", amount)
            return True
            
        print("Account Not Found")
        return False
    
    def withdraw(self, account_num, amount):
        account = self.check_account(account_num)
        if account:
            try:
                account.withdraw(amount)
                self.transaction_log(account_num, "Withdraw", amount)
                return True
                
            except:
                print("Balance Too Low")
                return False
                
                
            
              
        print("Account Not Found")
        return False


    def search_account(self, account_num):
        account = self.check_account(account_num)
        if account:
            print(account)
            return True
    
    def check_account(self, account):
        for accounts in self.accounts:
            if accounts.get_number() == account:
                return accounts
        print("Account Not Found")
        return False
    
    def transfer(self, account_num1, account_num2, amount ):
        account1 = self.check_account(account_num1)
        account2 = self.check_account(account_num2)
        if account1 and account2:        
            account1.withdraw(amount)
            self.transaction_log(account_num1, "Withdraw", amount)
            account2.deposit(amount)
            self.transaction_log(account_num2, "Deposit", amount)
            print("Tranfer Successful")
    
    def transaction_log(self, account_num, transaction_type, amount):
        self.transactions.append(Transaction(account_num, transaction_type, amount))
    
    def print_log(self):
        for transactions in self.transactions:
            print(transactions)
        

    
                        
                       
                        

            
a1 = Account(1234,"John", 200)
a2 = Account(4321,"Mike", 800)
bank = BankManager()
bank.add_account(a2)
bank.add_account(a1)

bank.transfer(1234, 4321, 10)
bank.search_account(1234)
bank.search_account(4321)

bank.print_log()