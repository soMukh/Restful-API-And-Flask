from flask import Flask

app=Flask(__name__)

@app.route('/user/<name>/age/<int:age>')
def user_info(name,age):
    return f"{name} is {age} years old."

if __name__ == '__main__':
    app.run(debug=True) 