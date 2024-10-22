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
        print(f"the user information:{self.first_name},\n{self.last_name},{self.email},{self.age},{self.is_rewards_member},{self.gold_card_points}")
    
first_user=user('fatma', 'dal', 'gamil.com',23)
print(first_user)
# invoking the display_info mathod for the first_user object
first_user.display_info('fatma','dalhoumi','fagmail.com',22)