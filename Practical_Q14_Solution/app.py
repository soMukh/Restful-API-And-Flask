from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/data')
def data():
    data={
        "name":"Soham",
        "city":"Mumbai",
        "age":24
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)