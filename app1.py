from flask import request
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h2>Hello, friends.</h2>"

@app.route("/hello1")
def hello1():
    return "<h2>Hello, friends! 1.</h2>"

@app.route("/hello2")
def hello2():
    return "<h2>Hello, friends! 2.</h2>"

@app.route("/test")
def test():
    a = 5+6
    return "{} + {} = {}".format(5,6,a)

@app.route("/test2")
def test2():
    data = int(request.args.get('x'))
    return "Square of {} is {}.".format(data,data**2)

if __name__ == "__main__":
    app.run(host="0.0.0.0")