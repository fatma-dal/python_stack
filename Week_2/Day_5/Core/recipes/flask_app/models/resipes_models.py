from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash



class Recipe :
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date=data['date']
        self.time=data['time']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.posted_by=""
    @classmethod
    def get_all(cls): 
        qurey="select *form recipe join users on   recipe.user_id = users.id;"
        results= connectToMySQL(DB).query_db(qurey)
        recipes=[] 
        for row in results :
            recipe = cls(row)
            recipe.posted_by=f"{row['first_name']}"
            recipes.append(recipe)
        return recipes
    @classmethod
    def create(cls,data):
        query="insert into recipe (name,description,instructions,date,time,user_id) values (%(name)s,%(description)s,%(instructions)s,%(date)s,%(time)s,%(user_id)s);"
        result=connectToMySQL(DB).query_db(query,data)
        return result 
    @classmethod
    def get_recipe_by_user(cls,data):
        query = "select * from recipe join users on recipe.user_id=users.id where recipe.id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        user=cls(results[0])
        user.posted_by=results[0]['first_name'] 
        return user


    @classmethod
    def get_recipe_by_id(cls,data):
        query = "select * from recipe where id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        recipe = Recipe(results[0])
        return recipe


    @staticmethod
    def validate_recipe( data ):
        is_valid = True
        if len(data['name'])< 3 :
            is_valid=False
            flash("name must contain at least 3 chracaters","name_validation")
        if len(data['description'])<3:
            is_valid=False
            flash("location must contain at least 3 chracaters","description_validation")
        if len(data['instructions'])<3:
            is_valid=False
            flash("Instructions must contain at least 3 characters","instructions_validation")
        return is_valid
    @classmethod 
    
    def update(cls,data) :
        query="update recipe set name=%(name)s,description=%(description)s,instructions=%(instructions)s,date=%(date)s,time=%(time)s WHERE  id=%(id)s ; "
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete(clas,data) :
        query="delet from recipe where id=%(id)s ;"
        return  connectToMySQL(DB).query_db(query,data)