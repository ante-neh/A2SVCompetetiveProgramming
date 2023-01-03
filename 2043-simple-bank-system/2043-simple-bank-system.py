class Bank:

    def __init__(self, balance: List[int]):
        self.book = balance
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 and account1 <= len(self.book) and 1 <= account2 and account2 <= len(self.book):
            if self.book[account1 - 1] >= money:
                self.book[account1 - 1] -= money
                self.book[account2 - 1] += money
                
                return True
            
            else:
                return False
            
        else:
            return False
        
    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account and account <= len(self.book):
            self.book[account - 1] += money
            
            return True
        
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account and account <= len(self.book):
            if self.book[account - 1] >= money:
                self.book[account - 1] -= money
                
                return True
            
            else:
                return False
            
        else:
            return False
        
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)