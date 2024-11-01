from flask import Flask,render_template

app=Flask(__name__)

@app.route('/play/<int:num>/<string:backgcolor>')
def renderboxes(num,backgcolor):
    return render_template('index.html' ,num=num ,backgcolor=backgcolor )


# @app.route('/')
# def get_table():
#     users = [
#     {'first_name' : 'Michael', 'last_name' : 'Choi'},
#     {'first_name' : 'John', 'last_name' : 'Supsupin'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
#     for key in range (users):
#         result=users.append(users['key'])

#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
