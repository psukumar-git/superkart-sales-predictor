import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

model_basename = 'superkart_model.joblib'

# Create the Flask app
flask_app = Flask('SuperKart Sales Predictor')

# Load the sales prediction model
sales_model = joblib.load(model_basename)

# Default - landing page
@flask_app.get('/')
def home():
  return 'This is the SuperKart Sales Predictor model'

# Endpoint for handling individual predictions
@flask_app.post('/v1/predict')
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

  # Convert the dictionary to a dataframe
  prod_data_df = pd.DataFrame([prod_data])

  # Predict using the loaded model
  sales_pred = sales_model.predict(prod_data_df).tolist()[0]

  # Return the test string
  return jsonify({'Sales prediction': sales_pred})

# Endpoint for batch predictions
@flask_app.post('/v1/predictbatch')
def predict_sales_batch():
  # Get the csv file with the batch of dependent features
  input_file = request.files['data_file']

  # Read the contents of the file
  batch_data = pd.read_csv(input_file)

  # Compute the log value for the allocated area and drop the original feature
  batch_data['Product_Allocated_Area_Log'] = np.log(batch_data['Product_Allocated_Area'])
  batch_data = batch_data.drop('Product_Allocated_Area', axis=1)

  # Predict the sales for the batch data
  batch_data['Predicted Sales'] = sales_model.predict(batch_data)

  # Drop the computed log feature before sending it back
  batch_data = batch_data.drop('Product_Allocated_Area_Log', axis=1)

  # Convert the dataframe to a dictionary and return the data
  batch_data_dict = batch_data.to_dict(orient='records')
  return batch_data_dict


# Run the Flask app
if __name__ == '__main__':
  flask_app.run(debug=True)
