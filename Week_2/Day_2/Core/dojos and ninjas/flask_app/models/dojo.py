from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models.ninja import Ninja

class Dojos :

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        dojos_from_db = connectToMySQL(DB).query_db(query)
        dojos = []
        for one_dojo in dojos_from_db:
            dojos.append(cls(one_dojo))
        return dojos
    
    def get_dojo(cls,dojo_id):
        query="SELECT * from  dojos where id=%(id)s;"
        results= connectToMySQL(DB).query_db(query,{'id': dojo_id})
        return cls(results[0])

    @classmethod
    def add_dojo (cls, data):
        query="INSERT INTO dojos (name) Value (%(name)s);"
        results= connectToMySQL(DB).query_db(query, data)
        return results 



    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DB).query_db( query , data )

        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo



