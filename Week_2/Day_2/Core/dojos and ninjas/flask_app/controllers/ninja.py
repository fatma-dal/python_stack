from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojos

@app.route('/ninjas')
def show_form():
    all_dojos=Dojos.get_all()
    return render_template('ninjas.html',all_dojos=all_dojos)

@app.route('/show/ninja')
def get_one_ninja():

    return render_template('show_ninjas.html')


@app.route('/create/ninja', methods=['POST'])
def add_ninja():
    ninjas_id=Ninja.add_ninjas(request.form)
    # print('ninjas******************************', ninjas)
    return redirect('show/ninja')

@app.route('/show/dojo/<int:dojo_id>')
def show(dojo_id):
    dojo=Dojos.get_dojo_with_ninjas({'id': dojo_id})

    return render_template("show_ninjas.html",dojo=dojo)








