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




