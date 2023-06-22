from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("converter/converter_home.html")

@app.route("/postman_converter", methods=["POST"])
def select_converter():
    if(request.method == "POST"):
        btn_selected = request.json["id"]
        if btn_selected == "btn_ctof_choice":
            return render_template("converter/ctof.html")
        if btn_selected == "btn_ftoc_choice":
            return render_template("converter/ftoc.html")
        if btn_selected == "btn_itof_choice":
            return render_template("converter/itof.html")
        if btn_selected == "btn_ftoi_choice":
            return render_template("converter/ftoi.html")
        
@app.route("/pman_ctof", methods=["POST"])
def ctof():
    if(request.method == "POST"):
        btn_selected = request.json["id"]
        if btn_selected == "btn_ctof_submit":
            temp_celcius = int(request.json["txt_celcius"])
            temp_fah = temp_celcius*9/5+32
            result="{} (in celcius) = {} (in fahrenheit)".format(temp_celcius,temp_fah)
            #return jsonify("converter/results.html",result=result)
            return render_template("converter/results.html", result=result)

@app.route("/pman_ftoc", methods=["POST"])
def ftoc():
    if(request.method == "POST"):
        btn_selected = request.json["id"]
        if btn_selected == "btn_ftoc_submit":
            temp_fah = int(request.json["txt_fahrenheit"])
            temp_celcius = (temp_fah-32)*5/9
            result="{} (in fahrenheit) = {} (in celcius)".format(temp_fah,temp_celcius)
            return jsonify(result)

@app.route("/pman_itof", methods=["POST"])
def itof():
    if(request.method == "POST"):
        btn_selected = request.json["id"]
        if btn_selected == "btn_itof_submit":
            height_inches = int(request.json["txt_inches"])
            height_feet = (height_inches * 0.0833)
            result="{} (inches) = {} (feet)".format(height_inches, height_feet)
            return jsonify(result)

@app.route("/pman_ftoi", methods=["POST"])
def ftoi():
    if(request.method == "POST"):
        btn_selected = request.json["id"]
        if btn_selected == "btn_ftoi_submit":
            height_feet = int(request.json["txt_feet"])
            height_inches = (height_feet * 12)
            result="{} (feet) = {} (inches)".format(height_feet, height_inches)
            return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
