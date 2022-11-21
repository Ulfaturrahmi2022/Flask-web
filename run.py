from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/list')
def list_data():
    return render_template('list.html')

@app.route('/input')
def input():
    return render_template('input.html') 

    if __name__=='__main__':
        app.run('127.0.0.1',2000,debug=True)

app.run()