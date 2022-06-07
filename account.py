from unicodedata import name


import csv
import os.path

class Account:
    def __init__(self):
        self.accounts = Account.objects()
        

    def withdraw(self):
        pass

    def deposit(self):
        pass

    @classmethod
    def objects(cls):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                accounts.append(Account(**dict(row)))
        return accounts


