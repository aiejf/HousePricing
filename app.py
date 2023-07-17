import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model
model=pickle.load(open('rf.pkl','rb'))
   
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    
    input_var=[i for i in request.form.values()]
    final_input_var=[np.array(input_var)]

    prediction = model.predict(final_input_var)

    output = round(prediction[0],2)

    return render_template('home.html', prediction_text='Sales prices should be $ {}'.format(output))     

# @app.route('/results', methods=['POST'])
# def results():
#     data=request.get_json(force=True)

#     predict=model.predict([np.array(list(data.values()))])
#     out=predict[0]
#     return jsonify(out)

if __name__=="__main__":
    app.run(debug=True)

