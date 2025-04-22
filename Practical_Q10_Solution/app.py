from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return f"Welcome to the Flask application!"

@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        "error":"Bad Request",
        "message":"The request could not be understood or was missing required parameters."
    }),400

@app.errorhandler(401)
def unauthorized(e):
    return jsonify({
        "error":"Unauthorized",
        "message":"You must be authenticated to access this resource."
    }),401

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error":"Not Found",
        "message":"The requested URL was not found on the server."
    }),404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "error":"Internal Server Error",
        "message":"An unexpected error occurred on the server."
    }),500

@app.errorhandler(503)
def service_unavailable(e):
    return jsonify({
        "error":"Service Unavailable",
        "message":"The server is temporarily unable to handle the request due to overload or maintenance."
    }),503

if __name__ == '__main__':
    app.run(debug=True)