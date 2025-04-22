from flask import Flask, session

app=Flask(__name__)
app.secret_key="supersecretkey"

@app.route('/login')
def login():
    session['user']='Soham'
    return "Logged in as user"

@app.route('/user')
def user():
    name=session.get('user')
    if not name:
        return "No user logged in"
    return f'{name} is logged in'

@app.route('/logout')
def logout():
    session.pop('user', None)
    return f'User logged out'

if __name__=='__main__':
    app.run(debug=True)