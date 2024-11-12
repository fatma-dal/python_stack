from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.resipes_models import Recipe
from flask_app.models.user_models import User
@app.route('/recipes')
def get_all():
    if 'user_id' not in session :
        return redirect('/')
    user=User.get_by_id({'id':session['user_id']})
    recipes=Recipe.get_all()
    return render_template('recipes.html',user=user,recipes=recipes)



@app.route('/recipes/new')
def display():
    if 'user_id' not in session :
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/create/recipe',methods=['POST'])
def add_recipe() :

    if Recipe.validate_recipe(request.form):
        data={
            **request.form,
            'user_id': session['user_id']
            }
        recipe_id=Recipe.create(data)
        return redirect('/recipes')
    return redirect ('/recipes/new')

@app.route('/recipes/<int:id>')
def display_user(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe=Recipe.get_recipe_by_user({'id':id})
    user= User.get_by_id({'id':session['user_id']})
    return render_template('chow.html',recipe=recipe,user=user)

@app.route('/recipe/edit/<int:id>')
def display_edit_page(id):
    if 'user_id' not in session :
        return redirect('/')
    recipe = Recipe.get_recipe_by_id({'id': id})
    print(recipe)
    return render_template('edit.html',recipe=recipe)


@app.route('/recipe/delete/<int:id>')
def delete(id):
    Recipe.delete({'id': id})
    return redirect('/recipes')

@app.route('/edit/recipe/<int:id>', methods=['POST'])
def update(id):
    if Recipe.validate_recipe(request.form):
        updated_recipe = {
            'id':id,
            **request.form
        }
        Recipe.update(updated_recipe) 
        return redirect('/recipes')
    return redirect('/recipe/edit/<int:id>')