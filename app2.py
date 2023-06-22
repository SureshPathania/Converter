from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<b>Company Name : ABC Corporation<br>Location : India<br> Contact Detail : 999-999-9999<br></b>"

@app.route("/welcome")
def welcome():
    return "<h3>Welcome to ABC Corporation</h3>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
