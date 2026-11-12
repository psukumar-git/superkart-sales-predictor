import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

model_basename = 'superkart_model.joblib'

# Create the Flask app
flask_app = Flask('SuperKart Sales Predictor')

# Load the sales prediction model
# pred_model = joblib.load(model_basename)

@flask_app.get('/')
def home():
  return 'This is the SuperKart Sales Predictor model'

@flask_app.post('/v1/onestore')
def predict_sales():
  # Get the JSON data and unpack it
  prod_data_json = request.get_json()
  prod_data = {
    'Product_Weight': prod_data_json['Product_Weight'],
    'Product_Sugar_Content': prod_data_json['Product_Sugar_Content'],
    'Product_Allocated_Area_Log': np.log(prod_data_json['Product_Allocated_Area']),
    'Product_MRP': prod_data_json['Product_MRP'],
    'Store_Size': prod_data_json['Store_Size'],
    'Store_Location_City_Type': prod_data_json['Store_Location_City_Type'],
    'Store_Type': prod_data_json['Store_Type'],
    'Product_Id_char': prod_data_json['Product_Id_char'],
    'Store_Age_Years': prod_data_json['Store_Age_Years'],
    'Product_Type_Category': prod_data_json['Product_Type_Category']
  }

  # Return the test string
  return jsonify(prod_data)

# Run the Flask app
if __name__ == '__main__':
  flask_app.run(debug=True)
