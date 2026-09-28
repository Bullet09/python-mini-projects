class Person:
    def __init__(self, name, age, id, account):
        self.name = name
        self.age = age
        self.id = id
        self.account = account


class Account:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
        self.transaction = []

    def add_transaction(self, transaction):
        self.transaction.append(transaction)
    


class Transaction:
    def __init__(self, transaction_id, amount, transaction_type, date):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date

