class BankAccount:
	
    def __init__(self,int_rate,balance):
        self.balance=balance
        self.int_rate=int_rate
	
    def deposit(self,amount):
        self.balance +=amount
        print("deposit amount=",amount,"now your balance = ",self.balance)
        return self
		
    def withdraw(self, amount):
        self.balance -=amount
        print("withdraw amount=",amount,"now your balance = ",self.balance)
        return self
		
    def display_account_info(self):
        print("your balance =",self.balance)
        return self
		
    def yield_interest(self):
        if self.balance>0:
            int=self.balance*self.int_rate
            self.balance+=int
            print("your balance =",self.balance)
            return self
A=BankAccount(0.01,100)
B=BankAccount(0.01,100)
A.deposit(10000).deposit(10000).deposit(10000).withdraw(99).yield_interest()
B.deposit(10000).deposit(10000).withdraw(1000).withdraw(99).withdraw(99).withdraw(99).yield_interest()
            
	