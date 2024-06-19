class Transaction:
    def __init__(self, account_num, transaction_type, amount):
        self.account_num = account_num
        self.transaction_type = transaction_type
        self.amount = amount
    
    def __str__(self):
        return f"Account Number: {self.account_num} - Transaction Type: {self.transaction_type} - Amount ${self.amount}"