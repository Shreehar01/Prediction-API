import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

'''import flask
from flask import request, jsonify
import json
'''

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    #return render_template('index.html')
    return "The server is up and running in the web you are seeing."
    
@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("Printing request")
    print(request.json)
    return 200, "Response"
    '''
    input_features = [float(x) for x in request.form.values()]
    final_features = [np.array(input_features)]
    prediction = model.predict(final_features)
    proba = model.predict_proba(final_features)
    output = round(prediction[0], 2)
    if output == 0:
        text = "The patient has low chance of having heart attack " + " with a probability of " + str(proba[0][1])
    else:
        text = "The patient has high chance of having heart attack."
    return jsonify(text)
    '''
    
    '''
    response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"result": "The type of iris plant is: " + types[prediction[0]]
				})
    '''

if __name__ == "__main__":
    app.run(debug=True)



    '''import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Machine Learning API for Heart Disease Prediction."

@app.route('/predict',methods=['POST'])
def predict():
    '''
    #For rendering results on HTML GUI
    '''
    try:
        input_features = [float(x) for x in request.form.values()]
        final_features = [np.array(input_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        text = ""
        if output == 0:
            text = "The patient has low chance of having heart attack."
        else:
            text = "The patient has high chance of having heart attack."
        result = [{"Output": text}]
        return jsonify(result)
    except: 
        return "Shreehar"

if __name__ == "__main__":
    app.run(debug=True)
    '''