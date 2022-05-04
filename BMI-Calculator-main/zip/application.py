from flask import Flask,render_template,request
import numpy as np
from pywebio.input import *
from pywebio.output import *

application= Flask(__name__)

@application.route("/")
def home():
    image = "i2.jfif"
    return render_template("bmiHome.html", image=image)

@application.route("/predict", methods=["GET", "POST"])

def predict():
    image = "res.jpg"
    height = request.form['height']
    weight = request.form['weight']
    #form_array= np.array([[height,weight]])

    h=int(height)
    w=int(weight)
    bmi=w/(h/100)**2
    example="{:.2f}".format(bmi)

    if (bmi<16):
        display =" Severely Underweight  !!"
    elif (bmi>=16 and bmi<18.5):
        display ="  Underweight !!"
    elif(bmi>=18.5 and bmi<25):
        display =" Perfect !!"
    elif (bmi>=25 and bmi <30):
        display = " Overweight !!"
    elif (bmi>=30 and bmi<35):
        display = " Moderateky Obese !!"
    elif (bmi>=35 ):
        display = " Severely Obese !!"

    value=str(example)
    result=display

    return render_template("bmiResult.html", value=value, result = result,image=image)
    
if __name__=='__main__':
    application.run(debug=True)