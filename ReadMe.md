#  Lagos Traffic Congestion Predictor
[Click here](https://lagos-traffic.streamlit.app) to access the app

Or copy this link, and open in another page: https://lagos-traffic.streamlit.app
## Overview

As a resident of Lagos, Nigeria's bustling economic hub, I and quite a number of other people have often found ourselves stuck in traffic, wasting time and fuel. Recognising the effect on traffic congestion on productivity, safety, and overall quality of life, I decided to leverage the skills i've garnered so far to try and solve this problem.

With frequent traffic bottlenecks in Lagos, especially around key zones like Ikeja and Berger, I built this predictive system to assist commuters in planning better routes, and contingencies ahead of traffic.
This app predicts traffic congestion levels — **Low**, **Medium**, or **High** ; howbeit still a prototype with potential for scalability.

This project is a machine learning-powered web app built with **Streamlit** that predicts traffic congestion levels in the **Ikeja–Berger axis of Lagos**, Nigeria. It uses custom features like route, weather, time of day, day of week, and holiday status to give real-time insights for better travel planning.

<img src="traffic_light.png" alt=Traffic Light width='300'/>


## What It Does

- Predicts **Low**, **Medium**, or **High** traffic congestion.
- Takes into account:
  - Selected Route
  - Weather Condition
  - Time of Day (AM/PM)
  - Day of the Week
  - Weekend & Public Holiday status
- Visually communicates results using colors.
- Easy-to-use interface.

## 🧠 Dataset(synthetic)
Due to poor data infrastructure in nigeria, I had no access to traffic data specific to Nigeria. I decided to be innovative and come up with one, that would simulate real-life conditions as close as possible.

Due to limited knowledge and expertise, the process of generating this synthetic dataset was quite rough, but it gets the job done.

The target variable was made to be in classes, rather than continuous(numerical), for easy interpretability for the users.

- **Features used**:
  - Route
  - Weather
  - Day
  - Hour
  - is_rush_hour
  - is_weekend
  - is_public_holiday
  - time_of_day
 
## **Tech Stack**

- **Frontend**: Streamlit
- **Backend/ML**: Scikit-learn, Pandas, XGBoost
- **Deployment**: To be hosted via Streamlit Cloud
- **Design Tools**: A png image(for traffic icon)


## 📁 Files

- `streamlit_app.py`: Streamlit application code
- `lagos_traffic_model.pkl`: Trained ML model
- `traffic_light.png`: Image used in UI
- `README.md`: Project documentation

The synthetic dataset was then cleaned, encoded using a pipeline, and used to train a basic classification model.

---

## **Machine Learning Model**

- Model Type: **XGBoost Classifier**
- Trained on: 3000 synthetic records
- Evaluation: Manually tested across time/weather scenarios
- Exported using `joblib` for use in the Streamlit app

## Goals
- Reduce travel time and stress for Lagos commuters
- Provide insights for urban planners
- Showcase the potential of Machine Learning and AI in addressing real-world problems

---

## ▶️ Run Locally

1. Clone the repo  | Install requirements | Run the App
```bash
git clone https://github.com/Olaolu22/Lagos-Traffic-Predictor.git
cd Lagos-Traffic-Predictor

pip install -r requirements.txt

streamlit run app.py
```
Link to app: https://lagos-traffic.streamlit.app
### Author
Built by **Olaoluwa**

3MTT Fellow ID: **FE/23/68321531**

Track: **AI/Machine Learning**

Cohort:**3**


**3MTT**

