from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
from flask_app import DB

class Ninja:
    def __init__(self,data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        



    @classmethod
    def get_ninjas (cls,data) :
        query="SELECT * from  ninjas ;"
        results= connectToMySQL(DB).query_db(query)
        ninjas=[]
        for ninja in results :
            ninjas.append(cls(ninjas))
        return ninjas

    @classmethod
    def get_one(cls,ninja_id):
        query="SELECT * from  ninjas where id=%(id)s;"
        results= connectToMySQL(DB).query_db(query,{'id': ninja_id})
        return cls(results[0])

    @classmethod
    def add_ninjas (cls,data):
        query="INSERT INTO ninjas (first_name,last_name,age,dojo_id) Value (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        results= connectToMySQL(DB).query_db(query,data)
        return results 
    

