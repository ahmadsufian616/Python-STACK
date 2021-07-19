class user :
    def __init__(self,name,email,acc_num):
        self.name=name
        self.email=email
        self.acc_num=acc_num
        self.acc= BankAccount(int_rate=0.02,balance=0)

    def make_withdrawal(self, amount):
        self.acc.withdraw(amount)

    def display_user_balance(self):
        print(self.acc.balance)

    def transfer_money(self, other_user, amount):
        self.acc_bal -=amount
        other_user.acc_bal+=amount
    def make_deposit(self, amount):	
    	self.acc.deposit(amount)
       
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


A=user("ahmad","a",111)
A.display_user_balance()
A.make_deposit(19999)

