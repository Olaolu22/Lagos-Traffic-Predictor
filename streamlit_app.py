import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Load model
model = joblib.load("lagos_traffic_model (1).pkl")
label_encoder = joblib.load('label_encoder.pkl')


# Defining biases again
route_bias = {
    'Ikeja-Alausa': 1.0,
    'Berger-Ojodu': 1.1,
    'Ikeja-ComputerVillage': 1.5,
    'Ojota-Ketu': 1.7,
    'Maryland-Palmgrove': 1.3
}

time_bias = {
    'morning_rush': 2.5,
    'midday': 1.2,
    'evening_rush': 2.8,
    'night': 0.7
}

weather_bias = {
    'sunny': 0.9,
    'rainy': 2.0,
    'cloudy': 1.2,
    'humid': 1.5
}


# Load image
st.image("traffic_light.png", width=200)


# Title
st.title("🚦 Lagos Traffic Congestion Predictor")

# Sidebar Info
st.sidebar.header("About")
st.sidebar.write("Predict traffic congestion levels in the Ikeja-Berger area using weather, time, day and other features.")
st.sidebar.markdown("""
---
Built by: Ogunsola Olaoluwa .....for the 3MTT Knowledge Showcase  
**Fellow ID:** FE/23/68321531  
**Cohort:** 3  
**Track:** AI/Machine Learning
""")

# options per parameter
routes = ['Berger-Ojodu', 'Ikeja-Alausa', 'Ikeja-ComputerVillage', 'Ojota-Ketu', 'Maryland-Palmgrove']
weather_options = ['sunny', 'rainy', 'humid', 'cloudy']
day_options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ampm_options = ['AM', 'PM']

def get_time_of_day(hour):
    if 6 <= hour <= 9:
        return "morning_rush"
    elif 10 <= hour <= 15:
        return "midday"
    elif 16 <= hour <= 20:
        return "evening_rush"
    else:
        return "night"

# Form
with st.form("prediction_form"):
    st.subheader("Input Parameters")

    route = st.selectbox("📍 Select Route", routes)
    #is_public_holiday = st.selectbox("🎉 Public Holiday?", ['No', 'Yes']) == 'Yes'
    is_public_holiday = st.checkbox("Is it a public holiday?")
    #is_weekend = st.selectbox("🛌 Weekend?", ['No', 'Yes']) == 'Yes'
    is_weekend = st.checkbox("Is it a weekend?")
    weather = st.selectbox("🌤 Weather Condition", weather_options)
    day_of_week = st.selectbox("📅 Day of Week", day_options)
    hour_input = st.number_input("⏰ Hour (1 to 12)", min_value=0, max_value=12, value=8)
    am_pm = st.selectbox("AM / PM", ampm_options)
    


    submit = st.form_submit_button("Predict Congestion Level")

# Submission and prediction
if submit:
    hour = hour_input if am_pm == 'AM' else hour_input + 12
    is_rush_hour = int((7 <= hour <= 9) or (16 <= hour <= 19))
    time_of_day = get_time_of_day(hour)

    base_score = (
        route_bias[route] * 
        time_bias[time_of_day] * 
        weather_bias[weather]
    )
    
    #modifiers 
    base_score += is_weekend * np.random.uniform(-0.3, 1.0)
    base_score += is_public_holiday * np.random.uniform(-0.2, 1.0)
    

    input_df = pd.DataFrame({
        'route': [route],
        'is_public_holiday': [is_public_holiday],
        'is_weekend': [is_weekend],
        'weather': [weather],
        'hour': [hour],
        'time_of_day':[time_of_day],
        'base_score':[base_score],
        'day': [day_of_week],
        'is_rush_hour': [is_rush_hour]
    })
 
    encoded_prediction = model.predict(input_df)
    #converting encoded data back to string(understandable) form
    prediction = label_encoder.inverse_transform(encoded_prediction)[0]


    st.markdown("### 🎯 Prediction Result")
    if prediction == 'Low':
        st.success("🟢 Congestion Level: Low ........... Enjoy your travels!")
    elif prediction == 'Medium':
        st.warning("🟡 Congestion Level: Medium ........... You may experience some delay.")
    else:
        st.error("🔴 Congestion Level: High ............ You are advised to stay home, or find alternative routes")

    