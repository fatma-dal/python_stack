class BankAccount :
    
    def __init__(self,intrest_rate,balance):
        self.intrest_rate=intrest_rate
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount
        return self
    # withdraw mathod : decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdrawl(self,amount):
        if amount>self.balance:
            print("Insufficient funds: Charging a $5")
            self.balance-=5
        else:
            self.balance-=amount
        return self
    # display_account_info mathod : print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    
    # yeield mathod:increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_intrest(self):
        while self.balance>0 :
            self.balance=self.balance*self.intrest_rate
        return self

# # tow account instances :
# account1= BankAccount(2,500)
# account2=BankAccount(5,80)
# # To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# account1.yield_intrest().deposit(5).deposit(5).deposit(5).withdraw(455)
# account2.deposit(2).deposit(552).withdraw(56).withdraw(787484).withdraw(56).withdraw(787484)






