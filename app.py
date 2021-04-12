class Buget(object):
    def __init__(self, category, amount):

        self.category = category
        self.amount = amount
        global total_balance
        total_balance = 0
        total_balance += self.amount

    def get_balance(self):
        return self.amount

    def make_deposit(self, deposit_amount):
        global total_balance
        self.amount = self.amount + deposit_amount
        total_balance += self.amount
        return self.amount

    def make_withdrawal(self, withdraw_amount):
        global total_balance
        self.amount = self.amount - withdraw_amount
        total_balance = self.amount - withdraw_amount
        return self.amount

    def make_transfer(self, destination, transfer_amount):
        global total_balance
        self.amount = self.amount - transfer_amount
        total_balance = self.amount + total_balance
        return self.amount

    def get_total_balance(self):
        global total_balance
        return total_balance


budet1 = Buget("Clothing", 200)
budet2 = Buget("Food", 500)
budet2.make_transfer(budet1, 2000)
print(budet2.get_total_balance())
