from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route('/home/<name>')
def home(name):
    return f"Welcome {name} to the Flask application!"

@app.route('/to-home')
def to_home():
    return redirect(url_for('home',name='User'))

if __name__ == '__main__':
    app.run(debug=True)