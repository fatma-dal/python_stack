from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo import Dojos

@app.route('/')
def index():
    all_dojos=Dojos.get_all()
    
    return render_template('dojos.html',all_dojos=all_dojos)

@app.route('/dojo/create' ,methods=['POST'])
def create_dojo():
    new_dojo=Dojos.add_dojo(request.form)
    return redirect ('/')





