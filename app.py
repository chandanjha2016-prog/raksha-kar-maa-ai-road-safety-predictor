# DISCLAIMER : ye educational/demo purpose ke liye hai.
# Real road safety decisions ke liye traffic rules aur experts ko follow karo.
# Model ka prediction 100% accurate nahi hota.
# Signature: chandan jha | RAKSHA KAR MAA - AI Road Safety Predictor | 2026


from flask import Flask, render_template, request,jsonify
from tensorflow.keras.models import load_model
import numpy as np
imort pickle

app = Flask(_name_)


# Model aur Scaler Load Karo

model = load_model('road_safety_model.h5')
scaler = pickle.load(open('scaler.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        #request.form use karo, get_json nahi
        speed = float(request.form['speed'])
        weather = int(request.formd['weather'])
        time_of_day = int(request.form['time_of_day'])
        driver_age = int(request.form['driver_age'])
        road_type = int(request.form['road_type'])
        alcohol_level = float(request.form['alcohol_level'])
    


    features = np.array([[speed, weather, time_of_day, driver_age, road_type, alcohol_level]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    risk_prob = float(prediction[0][0]) * 100


    result = "High Risk" if risk_prob > 50 else "Low Risk"


    return jsonifu({'prediction': f'{result}: {risk_prob:.2f}%'})

except Exception as e:
    return jsonify({'error': str(e)})


if_name_ == '_main-'
app,run(debug=True)

