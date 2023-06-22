from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("converter/converter_home.html")

@app.route("/select_converter", methods=["POST","GET"])
def select_converter():
    if request.form["btn_choice"] == "btn_ctof_choice":
        #return render_template("converter/ctof.html")
        return ("its ok")
    if request.form["btn_choice"] == "btn_ftoc_choice":
        return render_template("converter/ftoc.html")
    if request.form["btn_choice"] == "btn_itof_choice":
        return render_template("converter/itof.html")
    if request.form["btn_choice"] == "btn_ftoi_choice":
        return render_template("converter/ftoi.html")

@app.route("/pman_ctof", methods=["POST"])
def ctof():
    if(request.method == "POST"):
        temp_celcius = int(request.form["txt_celcius"])
        temp_fah = temp_celcius*9/5+32
        result="{} (in celcius) = {} (in fahrenheit)".format(temp_celcius,temp_fah)
        return render_template("converter/results.html", result=result)

@app.route("/pman_ftoc", methods=["POST"])
def ftoc():
    if(request.method == "POST"):
        temp_fah = int(request.form["txt_fahrenheit"])
        temp_celcius = (temp_fah-32)*5/9
        result="{} (in fahrenheit) = {} (in celcius)".format(temp_fah,temp_celcius)
        return render_template("converter/results.html", result=result)

@app.route("/pman_itof", methods=["POST"])
def itof():
    if(request.method == "POST"):
        height_inches = int(request.form["txt_inches"])
        height_feet = (height_inches * 0.0833)
        result="{} (inches) = {} (feet)".format(height_inches, height_feet)
        return render_template("converter/results.html", result=result)

@app.route("/pman_ftoi", methods=["POST"])
def ftoi():
    if(request.method == "POST"):
        height_feet = int(request.form["txt_feet"])
        height_inches = (height_feet * 12)
        result="{} (feet) = {} (inches)".format(height_feet, height_inches)
        return render_template("converter/results.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
