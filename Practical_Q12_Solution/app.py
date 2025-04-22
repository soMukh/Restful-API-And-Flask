from flask import Flask, render_template, request

app=Flask(__name__)

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/')
def reverse():
    return render_template('reverse.html',text='Welcome to Flask!')

if __name__=='__main__':
    app.run(debug=True)
