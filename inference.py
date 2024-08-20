Cross region replication

Reducing latency
backup
parallel computing
streaming platformsimport json
import joblib
import os
import numpy as np
import pandas as pd

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.pkl")  # Loading the model
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':
        
        input_data = json.loads(request_body)         
        
        # Ensuring correct data types for the input
        input_data['Store'] = np.int64(input_data['Store'])
        input_data['Holiday_Flag'] = np.int64(input_data['Holiday_Flag'])
        input_data['Month'] = np.int32(input_data['Month'])
        input_data['DayOfWeek'] = np.int32(input_data['DayOfWeek'])
        input_data['Temperature'] = np.float64(input_data['Temperature'])
        input_data['Fuel_Price'] = np.float64(input_data['Fuel_Price'])
        input_data['CPI'] = np.float64(input_data['CPI'])
        input_data['Unemployment'] = np.float64(input_data['Unemployment'])
        
        input_df = pd.DataFrame([input_data])  # Converting input to DataFrame
        
        expected_features = ['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Month', 'DayOfWeek']
        input_df = input_df[expected_features]
        
        return input_df
    else:
        return None

def predict_fn(input_data, model):
    prediction = model.predict(input_data)  # Making predictions
    return prediction

def output_fn(prediction, response_content_type):
    result = {'Predicted Weekly Sales': prediction[0]}
    return json.dumps(result)