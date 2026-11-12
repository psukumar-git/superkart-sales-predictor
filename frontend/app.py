import streamlit as st
import pandas as pd
import requests
import numpy as np

# Define the URL for the Flask backend app, with the port it's listening on
BACKEND_URL = 'http://backend:7860'

# Title
st.title('SuperKart Sales Predictor')
st.write('Enter the details of the product to predict the likely sales amount')

# Get the data for the various fields
store_type = st.selectbox('Store type:', ['Supermarket Type1', 'Supermarket Type2', 'Departmental Store', 'Food Mart'])
store_loc = st.selectbox('Store location city type:', ['Tier 1', 'Tier 2', 'Tier 3'])
store_size = st.selectbox('Store size:', ['Small', 'Medium', 'High'])
store_age = st.number_input('Age of the store, in years:', min_value=0)
prod_type_cat = st.selectbox('Product type:', ['Perishables', 'Non Perishables'])
prod_id = st.selectbox('Product ID:', ['FD', 'DR', 'NC'])
prod_sugar = st.selectbox('Sugar content:', ['Low Sugar', 'No Sugar', 'Regular'])
prod_area = st.number_input('Area allocated for product:', min_value=0.0, max_value=1.0)
prod_weight = st.number_input('Product weight:', min_value=0.0)
prod_mrp = st.number_input('Product MRP:', min_value=0.0)

# Create the JSON payload to send with the POST request
prod_data = {
  'Product_Weight': prod_weight,
  'Product_Sugar_Content': prod_sugar,
  'Product_Allocated_Area': prod_area,
  'Product_MRP': prod_mrp,
  'Store_Size': store_size,
  'Store_Location_City_Type': store_loc,
  'Store_Type': store_type,
  'Product_Id_char': prod_id,
  'Store_Age_Years': store_age,
  'Product_Type_Category': prod_type_cat
}

# If the Predict Sales button is clicked, send the POST request with the payload
if st.button('Predict Sales', type='primary'):
  response = requests.post(f'{BACKEND_URL}/v1/onestore', json=prod_data)

  if response.status_code == 200:
    # Received a successful response
    # Get the JSON payload
    result = response.json()

    st.success(result['Product_Allocated_Area_Log'])
