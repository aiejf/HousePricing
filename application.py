import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

application=Flask(__name__)

## Load the model
model=pickle.load(open('rf.pkl','rb'))
   
@application.route('/')
def home():
    return render_template("home.html")

@application.route('/predict', methods=['POST'])
def predict():
    
    input_var=[i for i in request.form.values()]
    final_input_var=[np.array(input_var)]

    prediction = model.predict(final_input_var)

    output = round(prediction[0],2)

    return render_template('home.html', prediction_text='Sales prices should be $ {}'.format(output))     

if __name__=="__main__":
    application.run(debug=True)

