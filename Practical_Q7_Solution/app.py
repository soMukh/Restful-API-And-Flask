from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/validate', methods=['POST'])
def submit():
    name=request.form['name']
    email=request.form['email']
    if not name or not email:
        return {"error":"Please fill in all fields."},400
    if '@' not in email or '.' not in email.split('@')[-1]:
        return {"error":"Please enter a valid email address."},400
    return f'Name:{name}, Email: {email}'

if __name__=='__main__':
    app.run(debug=True)