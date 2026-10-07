from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello, World!_print")
    return "<h1>Hello, World!</h1>"

@app.route('/html')
def html():
    return send_file('index.html')

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/services')
def services():
    name = 'John Doe'
    return f'Hello, {name}!'

@app.route('/contact')
def contact():
    return 'This is the contact page.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)