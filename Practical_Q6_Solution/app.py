from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    email=request.form['email']
    return f'Name:{name}, Email: {email}'

if __name__=='__main__':
    app.run(debug=True)