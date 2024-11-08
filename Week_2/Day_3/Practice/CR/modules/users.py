from mysqlconnection import connectToMySQL
class User :
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def read_all(cls):
        query='SELECT * FROM users;'
        result= connectToMySQL('workbenchsetup').query_db(query)
        all_users = []
        for one_user in result:
            all_users.append(cls(one_user))
        return all_users
    
    @classmethod
    def add_user(cls,data):
        query="INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
        results=connectToMySQL('workbenchsetup').query_db(query,data)
        return results




