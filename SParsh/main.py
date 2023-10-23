from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods =  ["GET", "POST"])
def eg():

    bmi_default = "zero"

    if request.method == "POST":
       
       weight = float(request.form.get("wgt"))
      
       height = float(request.form.get("hgt"))

       BMI = weight / height  

       return render_template('result.html', bmi =str(BMI))


    return render_template('result.html', bmi = bmi_default)



if __name__=='__main__':
    app.run(debug=True)