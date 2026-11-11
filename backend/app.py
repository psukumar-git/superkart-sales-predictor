
import joblib
import pandas as pd
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
  # Product_Type_Category, Store_Type
  prod_data = {
      'Product_Type_Category': prod_data_json['Product_Type_Category'],
      'Store_Type': prod_data_json['Store_Type']
  }

  # Build a test string
  test_string = f"In {prod_data['Store_Type']}, predicting {prod_data["Product_Type_Category"]}"

  # Return the test string
  return jsonify({'Prediction': test_string})

# Run the Flask app
if __name__ == '__main__':
  flask_app.run(debug=True)
