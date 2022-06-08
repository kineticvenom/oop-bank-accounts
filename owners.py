import csv
from account import Account

class Owner:
    def __init__(self, owner_id, last_name, first_name, street_address, city, state) :
        self.owner_id = owner_id
        self.name = last_name + f', {first_name}'
        self.address = f'{street_address} {city}, {state}'
        self.all_accounts = Account.all_accounts()
        

    def __str__(self):
        return f'ID: {self.owner_id} NAME: {self.name} ADDRESS: {self.address} '

    
    def owner_id(self):
        account_number = ''
        path = "support/account_owners.csv"
        with open(path) as csvfile:
            owner_ids = []
            reader = csv.reader(csvfile)
            for row in reader:
                # print(row)
                # print(owner)
                owner_ids.append(row)
        return owner_ids

    @classmethod
    def all_owners(cls):
        owners = []
        path = "support/owners.csv"
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                owner = Owner(row[0],row[1],row[2],row[3],row[4],row[5])
                # print(owner)
                owners.append(owner)
        return owners

# print(Owner.all_owners())
print(Owner.owner_id(1215))