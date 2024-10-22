class user:
    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        #default attributes
        self.is_rewards_member=False
        self.gold_card_points= 0
    def display_info(self, first_name,last_name,email,age,):
        print(f"the user information:{self.first_name},\n{self.last_name},\n{self.email},\n{self.age},\n{self.is_rewards_member},\n{self.gold_card_points}")
    
    # enroll + ninja bonuse
    def enroll(self):
        if self.is_rewards_member== True:
            print("User already a member")
            return False
        else:    
            print(f"is the status of the user is a member?  {self.is_rewards_member} \n gold card points : {self.gold_card_points}")
            self.is_rewards_member=True
            self.gold_card_points= 200
            return True

    # spend_points + ninja bonuse
    def spend_points(self,amount):
        if amount <= self.gold_card_points :
            spend=self.gold_card_points -amount
            print (f"Your current points : {spend}")
        else :
            print("Sorry! You don't have enough points.")


first_user=user('fatma', 'dal', 'gamil.com',23)
print(first_user)
# implementing the display_info mathod for the first_user object
first_user.display_info('fatma','dalhoumi','fagmail.com',22)

# implementing the enroll()
first_user.enroll()

#impelenting the spend_points()
first_user.spend_points(500)

