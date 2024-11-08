from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
    feedback = session.get('feedback', None)
    return render_template('index.html', feedback=feedback)

@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
    except ValueError:
        session['feedback'] = "Please enter a valid number."
        return redirect('/')
    
    random_number = session['random_number']
    
    
    if guess < random_number:
        session['feedback'] = "Too low! Try again."
    elif guess > random_number:
        session['feedback'] = "Too high! Try again."
    else:
        session['feedback'] = "Correct! You guessed the number!"
        # Reset the game after a correct guess
        session.pop('random_number', None)
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
