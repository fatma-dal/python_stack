from flask import Flask,render_template 
app=Flask(__name__)
from modules.users import User

@app.route('/')
def show_all():
    users_list=User.read_all()
    return render_template('Read.html',users= users_list)






if __name__=="__main__":
    app.run(debug=True)