#  Lagos Traffic Congestion Predictor
[Click here](https://lagos-traffic.streamlit.app) to access the live app

Or copy this link, and open in another page: https://lagos-traffic.streamlit.app

[The ipynb notebook is also here](https://colab.research.google.com/drive/1FgS-DdIIvehf8PTx6erTB1TlxMLk3LG4#scrollTo=2Y6bFySxVLg9)

You can as well copy this link: https://colab.research.google.com/drive/1FgS-DdIIvehf8PTx6erTB1TlxMLk3LG4#scrollTo=2Y6bFySxVLg9
## Overview

As a resident of Lagos, Nigeria’s bustling economic hub, I’ve often found myself stuck in traffic — wasting valuable time, fuel, and energy. Recognizing how congestion affects productivity, safety, and well-being, I decided to apply the AI/ML skills I’ve gained so far to try to predict traffic congestion and help people plan better.

This project is a machine learning-powered web app built with **Streamlit** that predicts traffic congestion levels in the **Ikeja–Berger axis of Lagos**, Nigeria.

The web app predicts traffic congestion levels — Low, Medium, or High — using features like route, time of day, weather, and holiday status.

Though still a prototype, this app has great potential for real-world adoption and scalability.



<img src="traffic_light.png" alt=Traffic Light width='300'/>


## What the App Does

- Predicts Lagos traffic congestion as **Low**, **Medium**, or **High**
- Accepts user inputs like:
  - Selected Route
  - Weather Condition
  - Time of Day (AM/PM)
  - Day of the Week
  - Weekend & Public Holiday status
- Visually communicates results using colour codes.
- Simple and user-friendly interface


## Dataset(synthetic)
Due to poor data infrastructure in Nigeria, I couldn't find a reliable, open-source dataset for Lagos traffic. I decided to create a synthetic dataset that simulates realistic traffic patterns based on:

- Personal observation of traffic trends in Lagos

- Assumptions around peak hours, holidays, and weather influence

- Though manually generated and not perfect, the dataset captures useful trends for model training.

**Features included:**

- Route
- Weather
- Day
- Hour
- is_rush_hour
- is_weekend
- is_public_holiday
- time_of_day
- Target variable: Categorical — Low, Medium, High congestion.


 
## **Tech Stack**

- **Frontend**: Streamlit
- **Backend & ML**: Python, Scikit-learn, XGBoost, Pandas
- **Deployment**: Streamlit Cloud
- **Design**: Custom PNG image for traffic light indicator

## 📁 Files

- `streamlit_app.py`: Streamlit application code
- `lagos_traffic_model(1).pkl`: Trained ML model
- `traffic_light.png`: Visual for output display
- `README.md`: Project documentation
- `label_encoder.pkl`: Encodes the target variable for processing by the model


---

## **Machine Learning Model**

- Model: XGBoost Classifier
- Training size: ~3000 synthetic entries
- Preprocessing: Label encoding & pipeline
- Export: joblib for deployment
- Evaluation: Manually tested using common traffic scenarios

## Goals
- Help Lagos residents reduce time spent in traffic
- Empower people to plan better journeys
- Showcase the potential of Machine Learning and AI in addressing real-world problems
- Lay groundwork for future expansion into real-time prediction with live traffic data



---

## ▶️ Run Locally

1. Clone the repo  | Install requirements | Run the App
```bash
# Clone the repo
git clone https://github.com/Olaolu22/Lagos-Traffic-Predictor.git
cd Lagos-Traffic-Predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

```
### Author
Built by: **Ogunsola Olaoluwa**

Fellow ID: **FE/23/68321531**

Cohort: **3**

Track: **AI / Machine Learning**

Program: **3MTT Nigeria**


I built everything from scratch (a very tiring process, might I add) — including the synthetic dataset, model pipeline, and UI — without using AI tools. This project represents my growth, creativity, and ability to apply what I’ve learned.

---
Thank you for taking the time to review this project. I believe this is only the beginning of how we can use technology to solve uniquely Nigerian challenges. Your feedback is welcome!


**3MTT**

