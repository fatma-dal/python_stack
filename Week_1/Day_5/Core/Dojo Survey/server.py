from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a random secret key for session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Store form data in the session
    session['name'] = request.form.get('name')
    session['email'] = request.form.get('email')
    session['gender'] = request.form.get('gender')
    session['interests'] = request.form.getlist('interests')  # Stores selected checkboxes
    
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
