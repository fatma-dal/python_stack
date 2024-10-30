from flask import Flask,render_template

app=Flask(__name__)

@app.route('/play/<int:num>/<string:backgcolor>')
def renderboxes(num,backgcolor):
    return render_template('index.html' ,num=num ,backgcolor=backgcolor )


if __name__ == "__main__":
    app.run(debug=True)
