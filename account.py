""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Account:
    def __init__(self, number, name, balance):
        self.set_number(number)
        self.set_name(name)
        self.set_balance(balance)
    
    def set_number(self, new_number):
        if new_number == "":
            raise ValueError("Name Cannot Be Empty")    
        self._number = new_number

    
    def get_number(self):
        return self._number

    def set_name(self, new_name):
        if new_name == "":
            raise ValueError("Name Cannot Be Empty")    
        self._name = new_name

    def get_name(self):
        return self._name

    def set_balance(self, new_balance):
            if new_balance < 0:
                raise ValueError("Initial Balance Cannot Be Negative")
            self._balance = new_balance


    def get_balance(self):
        return f"${self._balance:.2f}"



    def __str__(self):
        return f"Account Number:{self.get_number()}, {self.get_name()} {self.get_balance()}"
    
    def deposite(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}")
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Account Balance Too Low")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}")




