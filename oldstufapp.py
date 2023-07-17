# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query-example')
def query_example():
    language=request.args.get('language')
    framework=request.args.get('framework')
    return '''<h1>the language value is : {} </h1>
              <h1>the framework value is : {} </h1>'''.format(language,framework)

# allow both GET and POST requests
@app.route('/form-example', methods=['POST','GET'])
def form_example():
    
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                    <h1>The language value is: {}</h1>
                    <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True)#, port=5000)


# import json
# import pickle

# from flask import Flask,request,app,jsonify,url_for,render_template
# import numpy as np
# import pandas as pd

# app=Flask(__name__)

# ## Load the model
# model=pickle.load(open('rf.pkl','rb'))
   
# @app.route('/')
# def home():
#     return render_template("home.html")

# @app.route('/predict', methods=['POST'])
# def predict():

#     CRIM=request.form.get('CRIM')
#     ZN=request.form.get('ZN')
#     INDUS=request.form.get('INDUS')
#     CHAS=request.form.get('CHAS')
#     NOX=request.form.get('NOX')
#     RM=request.form.get('RM')
#     Age=request.form.get('Age')
#     DIS=request.form.get('DIS')
#     RAD=request.form.get('RAD')
#     TAX=request.form.get('TAX')
#     PTRATIO=request.form.get('PTRATIO')
#     B=request.form.get('B')
#     LSTAT=request.form.get('LSTAT')

#     input_var=[CRIM,ZN,INDUS,CHAS,NOX,RM,Age,DIS,RAD,TAX,PTRATIO,B,LSTAT]
#     final_input_var=[np.array(input_var)]

#     prediction = model.predict(final_input_var)

#     output = prediction

#     return render_template('home.html', prediction_text='Sales prices should be $ {}'.format(output))     

# @app.route('/results', methods=['POST'])
# def results():
#     data=request.get_json(force=True)
#     predict=model.predict([np.array(list(data.values()))])
#     out=predict[0]
#     return jsonify(out)

# if __name__=="__main__":
#     app.run(debug=True)