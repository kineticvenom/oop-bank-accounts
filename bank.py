from account import Account

class Bank:
    def __init__(self):
        self.accounts = Account.all_accounts()