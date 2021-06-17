# Importing libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle

# Initializing the flask and cors.
app = Flask(__name__)
CORS(app)

model_heart = pickle.load(open('heart-attack-model.pkl', 'rb'))
model_diabetes = pickle.load(open('diabetes-model.pkl', 'rb'))
model_stroke = pickle.load(open('stroke-model.pkl', 'rb'))
#model_credit = pickle.load(open('credit-model.pkl', 'rb'))
model_loan = pickle.load(open('loan-model.pkl', 'rb'))
model_insurance = pickle.load(open('insurance-model.pkl', 'rb'))

# Homepage
@app.route('/')
def home():
    #return render_template('index.html')
    return jsonify({"response": "This is homepage."})


# Heart Prediction
@app.route('/heart-prediction', methods=['POST'])
def predict_heart():    
    data = request.get_json()
    prediction_data = []
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


# Stroke Prediction
@app.route('/stroke-prediction', methods=['POST'])
def predict_stroke():
    print("Executed")    
    data = request.get_json()
    prediction_data = []
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
    
    prediction_val = model_stroke.predict(final_features)
    probability = model_stroke.predict_proba(final_features)[0][1]
    output = round(prediction_val[0], 2)
    if probability < 0.5:
        text = "Low Chance"
    else:
        text = "High Chance"
    data['probability'] = round(probability, 2)
    data['prediction'] = text
    return jsonify(data)


# Diabetes Prediction
@app.route('/diabetes-prediction', methods=['POST'])
def predict_diabetes():    
    data = request.get_json()
    prediction_data = []
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
    
    prediction_val = model_diabetes.predict(final_features)
    probability = model_diabetes.predict_proba(final_features)[0][1]
    output = round(prediction_val[0], 2)
    if probability < 0.5:
        text = "Low Chance"
    else:
        text = "High Chance"
    data['probability'] = probability
    data['prediction'] = text
    return jsonify(data)

'''
# Credit Card Approval Prediction
@app.route('/credit-prediction', methods=['POST'])
def predict_credit():    
    data = request.get_json()
    print("Right above", data)
    prediction_data = []
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
    print('Reached 153')
    prediction_val = model_credit.predict(final_features)
    print("Reached 154") 
    probability = model_credit.predict_proba(final_features)[0][1]
    output = round(prediction_val[0], 2)
    if probability < 0.5:
        text = "Low Chance"
    else:
        text = "High Chance"
    data['probability'] = probability
    data['prediction'] = text
    data['probability'] = 0.4
    data['prediction'] = "High Chance"
    return jsonify(data)
    
'''

# Loan Approval
@app.route('/loan-prediction', methods=['POST'])
def predict_loan():    
    data = request.get_json()
    prediction_data = []
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
    
    prediction_val = model_loan.predict(final_features)
    probability = model_loan.predict_proba(final_features)[0][1]
    output = round(prediction_val[0], 2)
    if probability < 0.5:
        text = "Low Chance"
    else:
        text = "High Chance"
    data['probability'] = probability
    data['prediction'] = text
    return jsonify(data)


# Insurance Premium Prediction
@app.route('/insurance-prediction', methods=['POST'])
def predict_insurance():    
    data = request.get_json()
    print(data)
    prediction_data = []
    delete_list = ['createdAt', 'creator', '__v', 'update', 'prediction', 'value']
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
    prediction_val = model_insurance.predict(final_features)
    print(prediction_val)
    if prediction_val[0] > 9700:
        text = "High Premium"
    else:
        text = "Low Premium"
    data['value'] = round(prediction_val[0], 2)
    data['prediction'] = text
    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)


