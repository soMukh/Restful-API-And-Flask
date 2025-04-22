from flask import Flask,request

app=Flask(__name__)
students=[]

@app.route('/student/students', methods=['GET'])
def get_students():
    return {'students': students}, 200

@app.route('/student/add', methods=['POST'])
def add_student():
    data=request.get_json()
    name=data.get('name')
    if not name:
        return {'error': 'Name is required'}, 400
    students.append(name)
    return {'message': 'Student added successfully'}, 201

if __name__ == '__main__':
    app.run(debug=True)