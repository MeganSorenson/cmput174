class Account:
    def __init__(self, acc_id, acc_balance):
        # initializes the instance attributes
        # self is the Account object
        # acc_id is of type str
        # acc_balance is of type float
        self.account_id = acc_id
        self.account_balance = acc_balance

    def deposit(self, deposit_amount):
        self.account_balance += deposit_amount

    def withdraw(self, withdraw_amount):
        processed = False
        if withdraw_amount <= self.account_balance:
            processed = True
            self.account_balance -= withdraw_amount
        return processed

    def display(self):
        print("Account Number: " + self.account_id +
              " Balance: " + str(self.account_balance))

    def transfer(self, account_to, transfer_amount):
        result = self.withdraw(transfer_amount)
        if result == True:
            account_to.deposit(transfer_amount)


def main():
    accountA = Account("123ABC", 500)
    accountA.display()
    accountB = Account("123BCD", 1000)
    accountB.display()

    accountA.deposit(300)
    accountB.withdraw(200)
    print("After deposit to accountA ")
    accountA.display()
    print("After withdrawing from accountB ")
    accountB.display()

    print("After transfer from accountA to accountB ")
    accountA.transfer(accountB, 500)
    accountA.display()
    accountB.display()

    accountC = Account("123CDE", 2000)
    print("After transfer from accountC to accountA")
    accountC.transfer(accountA, 1000)
    accountA.display()
    accountC.display()


main()
