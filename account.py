from unicodedata import name


import csv
import os.path

class Account:
    def __init__(self, id, balance, date):
        self.id = id
        self.balance = balance
        self.date = date
    
    def __str__(self):
        return f"{self.id}, {self.balance}"

    def withdraw(self):
        pass

    def deposit(self):
        pass

    @classmethod
    def all_accounts(cls):
        accounts = []
        path = "support/accounts.csv"
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                account = Account(row[0],row[1],row[2])
                print(account)
                accounts.append(account)
        return accounts

    def find(self, id):
        pass
        



print(Account.all_accounts())
# print(bob)