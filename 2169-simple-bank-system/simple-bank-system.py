class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1-1 >= self.n or account2-1 >= self.n: # not valid account
            return False

        # if account has enough money to trasnfer
        if self.balance[account1 - 1] >= money:
            self.balance[account2 -1] += money
            self.balance[account1  - 1] -= money
            return True
        else: # if account hasn't enough money to trasnfer
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account -1 < self.n:   # if valid account
            self.balance[account-1] += money  # add the money to the account
            return True

        return False  # if not valid account

    def withdraw(self, account: int, money: int) -> bool:
        if account-1 < self.n and self.balance[account-1] >= money:
            self.balance[account-1] -= money # subtrack the money to the account
            return True

        return False  # if not valid account

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)