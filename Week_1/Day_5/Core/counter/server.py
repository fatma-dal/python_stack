from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret123'

# @app.route('/')
# def main():
#     return render_template('index.html')


@app.route('/', methods=['GET'])
def display_counter():
    
    if 'counter' not in session:
        session['counter'] = 0  

    return render_template('counter.html', counter=session['counter'])

@app.route('/', methods=['POST'])
def update_counter():
    session['counter'] += 1  
    return redirect('/')

@app.route('/reset')
def reset_counter():
    session.clear()  
    return redirect('/')  


if __name__ == '__main__':
    app.run(debug=True)
