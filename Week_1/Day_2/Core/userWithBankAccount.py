from BankAccount import BankAccount

class User:
    def __init__(self,name, age , id  ):
        self.name=name
        self.age=age
        self.id=id
        # self.account=BankAccount(intrest_rate=intrest_rate,balance=balance)
        self.account=[BankAccount(intrest_rate=10,balance=55)] #list of accounts

    #methods    
    def add_account(self,intrest_rate,balance):
        self.account.append(BankAccount(intrest_rate,balance))
        return f"New account with balance {balance} and interest rate {intrest_rate} added."



    def make_deposit(self,amount,account_index):
        self.account[account_index].deposit(amount)
        return f"Transaction has successfully done! in your account my account {self.account[account_index]}."

    def make_withdrawal(self,index,amount):
        self.account[index].withdrawl(amount)
    
    def display_user_balance(self,index):
        self.account[index].display_account_info()


user1=User('alice','42',125547)
user1.add_account(125,554)
user1.add_account(11,55)
user1.display_user_balance(0)

for acc in user1.account:  #display all accounts of user1
    acc.display_account_info()



