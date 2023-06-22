from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index_postman.html")

@app.route("/postman_action", methods=["POST"])
def math_ops1():
    if(request.method == "POST"):
        ops=request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
        if ops == "add":
            r = num1+num2
            result="{} + {} = {}".format(num1,num2,r)
        if ops == "subtract":
            r = num1-num2
            result="{} - {} = {}".format(num1,num2,r)
        if ops == "multiply":
            r = num1*num2
            result="{} * {} = {}".format(num1,num2,r)
        if ops == "divide":
            r = num1/num2
            result="{} / {} = {}".format(num1,num2,r)
        return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
