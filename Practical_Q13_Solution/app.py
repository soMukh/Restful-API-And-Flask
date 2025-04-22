from flask import Flask,request,redirect,url_for

app=Flask(__name__)

@app.route('/home')
def home():
    return redirect(url_for('welcome',name='Soham'))

@app.route('/welcome')
def welcome():
    name=request.args.get('name')
    return f"Welcome {name} to the Flask application!"

if __name__ == '__main__':
    app.run(debug=True)