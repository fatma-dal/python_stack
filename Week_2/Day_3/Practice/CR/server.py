from flask import Flask,render_template , redirect,request
app=Flask(__name__)
from modules.users import User

@app.route('/users')
def show_all():
    users_list=User.read_all()
    return render_template('Read.html',users= users_list)

@app.route('/users/new')
def show_form():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def add_user():
    User.add_user(request.form)
    return redirect('/users')







if __name__=="__main__":
    app.run(debug=True)