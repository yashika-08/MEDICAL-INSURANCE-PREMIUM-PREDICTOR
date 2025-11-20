import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

model = pkl.load(open('MIPML.pkl','rb'))

st.header('Medical Insurance Premium Predictor')



gender = st.ectbselox('Choose Gender',['Female','Male'])
smoker = st.selectbox('Do you Smoke?',['Yes','No'])
region = st.selectbox('Which Region you Belong to?',['SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.slider('Enter Age', 5, 80)
bmi = st.slider('Enter Body Mass Index (BMI)', 5, 100)
children = st.slider('Choose Number of Kids of have?', 0, 5)

if gender == 'Female':
    gender = 0
else:
    gender = 1
    
if smoker == 'Yes':
    smoker = 0
else:
    smoker = 1
     
if region == 'SouthEast':
    region = 0
elif region == 'SouthWest':
    region = 1
elif region == 'NorthEast':
    region = 2
else:
    region = 3

input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)

if st.button('Predict'):
    predicted_premium = model.predict(input_data)
    display_string ='Insuarance Premium will be ' + str(round(predicted_premium[0],2)) + ' Ruppees'
    st.markdown(display_string)
    
# Run command python -m streamlit run app.py to run the file