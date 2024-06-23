""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account
from bank import BankManager
from utility import get_int
import os
import time

def add_account_ui(bank):
    number = get_int("Enter the Account Number:")
    name = input("Enter the Acount Holder:")
    balance = get_int("Enter the Account Balance:")
    bank.add_account(Account(number, name, balance))
    print()
    print(f"Acount: {number}, Added to Bank")

def withdraw_ui(bank):
    account_num = get_int("Enter the Account Number:")
    amount = get_int("Enter the Amount to Withdraw:")
    if bank.withdraw(account_num, amount):
        print(f"Withdrew:${amount}")
       
def deposit_ui(bank):
    account_num = get_int("Enter the Account Number:")
    amount = get_int("Enter the Amount to Deposit:")
    if bank.deposit(account_num, amount):
        print(f"Deposited:${amount}")


def transfer_ui(bank):
    account_num1 = get_int("Enter the Account Number:")
    account_num2 = get_int("Enter Recipients Account Number:")
    amount = get_int("Enter the Amount to Transfer:")
    if bank.transfer(account_num1, account_num2, amount):
        print(f"Transfered:${amount} to {account_num2}")

        
def search_account_ui(bank):
    account_num = get_int("Enter the Account Number:")
    if bank.search_account(account_num):
        input("Press Enter to Continue")

def print_log_ui(bank):
    print("Tranaction Log")
    print()
    bank.print_log()
    input("Enter to Continue:")

def main():


    bank = BankManager()

    actions = {'1': add_account_ui, '2': withdraw_ui, '3': deposit_ui, '4': transfer_ui, '5': search_account_ui,'6': print_log_ui}
   
    os.system('cls')
    
    while True:
        print(f"Bank Management System")
        print("1. Add Account")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Search")
        print("6. Transaction Log")
        print("7. Exit")

        act_choice = input("Enter choice: ")
        print()


        if act_choice == '7':
            print("Exiting Bank")
            time.sleep(1)
            os.system('cls')
            break
        elif act_choice in actions:
            actions[act_choice](bank)
        else: 
            print("Invalid Choice")
        time.sleep(2)
        os.system('cls')


        

if __name__ == "__main__":
    main()