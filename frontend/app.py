import streamlit as st
import pandas as pd
import requests

# Define the URL for the Flask backend app, with the port it's listening on
BACKEND_URL = 'http://backend:7860'

# Title
st.tite('SuperKart Sales Predictor')
st.write('Enter the details of the product to predict the likely sales amount')

# Get the data for the various fields
prod_type_cat = st.selectbox('Enter the product type:', ['Perishables', 'Non Perishables'])

store_type = st.selectbox('Enter the store type:', ['Supermarket Type1', 'Supermarket Type2', 'Departmental Store', 'Food Mart'])

# Create the JSON payload to send with the POST request
prod_data = {
    'Product_Type_Category': prod_type_cat,
    'Store_Type': store_type
}

# If the Predict Sales button is clicked, send the POST request with the payload
if st.button('Predict Sales', type='primary'):
  response = requests.post(f'{BACKEND_URL}/v1/onestore', json=prod_data)

  if response.status_code == 200:
    # Received a successful response
    # Get the JSON payload
    result = response.json()

    st.success(result['Prediction'])
