
from flask import Flask , render_template 
app=Flask(__name__)

@app.route('/')
def full_checkboard():
    return render_template('index.html')

@app.route('/<int:row>')
def add_rows(row):
    return render_template('custom.html', row=row)









if __name__ == '__main__':
    app.run(debug=True)

