from unicodedata import name


import csv


class Account:
    def __init__(self, id, balance, date):
        self.id = id
        self.balance = balance
        self.date = date
    
    def __str__(self):
        return f"{self.id}, {self.balance}"

    def withdraw(self,amount):
        # print(type(self.balance))
        if self.balance > amount :
            self.balance = int(self.balance) - int(amount)
            return f'Your new balance is : {self.balance}'
        else:
            return f'Insufficient funds! Currant Balance: {self.balance}' 

    def deposit(self, amount):
        self.balance = int(self.balance) + int(amount)
        return f'Your new balance is : {self.balance}'
    
    @classmethod
    def all_accounts(cls):
        accounts = []
        path = "support/accounts.csv"
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                account = Account(row[0],row[1],row[2])
                # print(account)
                accounts.append(account)
        return accounts

    def find(id):
        for account in Account.all_accounts():
            # print(account.id)
            if account.id == id :
                # print(account)
                return account
        
        



# print(Account.all_accounts())
# print(Account.find('15156'))

# bob = Account.find('15156')
# print(bob)
# print(bob.deposit('200'))