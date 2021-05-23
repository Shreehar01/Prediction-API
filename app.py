import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle

'''import flask
from flask import request, jsonify
import json
'''

app = Flask(__name__)
CORS(app)
model_heart = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    #return render_template('index.html')
    return jsonify({"response": "This is homepage."})





@app.route('/heart-prediction', methods=['POST'])
def predict_finance():
    
    data = request.get_json()
    prediction_data = []
    print(data.keys())
    delete_list = ['createdAt', 'creator', '__v', 'update', 'prediction', 'probability']
    for entries in delete_list:
        try:
            data.pop(entries)
        except:
            continue
    print(data.keys())
    for keys in data:
        if len(data[keys]) == 0:
            prediction_data.append(0)
        elif keys == 'name' or keys  == "_id":
            continue
        else:
            prediction_data.append(float(data[keys]))
    
    final_features = [np.array(prediction_data)]   
    
    prediction_val = model_heart.predict(final_features)
    probability = model_heart.predict_proba(final_features)[0][1]
    output = round(prediction_val[0], 2)
    print("This is the output" + str(output))
    if probability < 0.4:
        text = "Low Chance"
    elif probability >= 0.4 and probability < 0.6:
        text = "Moderate Chance"
    else:
        text = "High Chance"
    data['probability'] = probability
    data['prediction'] = text
    print(text)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)


