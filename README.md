# 🚖 NYC Taxi Trip Duration Prediction

## 📌 Project Overview

The **NYC Taxi Trip Duration Prediction** project aims to estimate the duration of taxi trips in New York City using historical trip records and machine learning techniques. Accurate trip duration prediction can improve route planning, customer experience, fleet management, and operational efficiency for ride-hailing and taxi services.

This project follows a complete end-to-end Machine Learning workflow, starting from data understanding and preprocessing to model deployment using **FastAPI** and **Streamlit**.

---

## 🎯 Problem Statement

Predicting taxi trip duration is a regression problem influenced by several factors such as pickup location, dropoff location, travel distance, pickup time, passenger count, and traffic conditions.

The objective of this project is to develop a robust machine learning model capable of accurately predicting trip duration using engineered features derived from the available trip data.

---

## 🎯 Objectives

- Understand and explore the NYC Taxi Trip dataset.
- Perform data cleaning and preprocessing.
- Engineer meaningful features such as travel distance and datetime-based attributes.
- Train and compare multiple regression algorithms.
- Optimize the best-performing model using RandomizedSearchCV.
- Interpret model performance through evaluation metrics and feature importance.
- Deploy the trained model using FastAPI.
- Develop an interactive web application using Streamlit for real-time predictions.

---

# 📂 Dataset

The project uses the **NYC Taxi Trip Duration Dataset** provided by Kaggle.

Dataset contains information such as:

- Vendor ID
- Pickup Date & Time
- Pickup Latitude & Longitude
- Dropoff Latitude & Longitude
- Passenger Count
- Store and Forward Flag
- Trip Duration (Target Variable)

---

# 🏗️ Project Structure

```
NYC_trip_duration/
│
├── backend/
│   ├── app.py
│   ├── predictor.py
│   ├── schemas.py
│   └── __init__.py
│
├── frontend/
│   ├── app.py
│   └── __init__.py
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── processed/
│
├── models/
│   ├── xgboost_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_interpretation_and_analysis.ipynb
│
├── src/
│   ├── config.py
│   ├── feature_engineering.py
│   └── __init__.py
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── LICENSE
```

---

# 🔄 Machine Learning Workflow

```
Dataset
   │
   ▼
Data Understanding
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Hyperparameter Tuning
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization
   │
   ▼
FastAPI Backend
   │
   ▼
Streamlit Frontend
```

---

# 🤖 Machine Learning Models

The following regression algorithms were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor (Optimized)

After comparing the performance of all models, the optimized **XGBoost Regressor** was selected as the final deployment model.

---

# 📊 Model Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# ⚙️ Feature Engineering

The following features were created during preprocessing:

- Pickup Hour
- Pickup Day
- Pickup Month
- Pickup Weekday
- Pickup Year
- Bearing
- Haversine, Manhattan Distance
- Encoded Store and Forward Flag

---

# 🚀 Deployment

The project is deployed locally using:

### Backend

- FastAPI

### Frontend

- Streamlit

The frontend collects trip information from the user and sends it to the FastAPI backend, which performs feature engineering, loads the trained model, and returns the predicted trip duration.

---

# 📂 Dataset

This project uses the **NYC Taxi Trip Duration** dataset from Kaggle.

Download the dataset from:

🔗 https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data?select=train.zip

After downloading, place the dataset files in: data/raw/

---

# 💻 Installation

Move to the project directory

```bash
cd NYC_trip_duration
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn backend.app:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit

```bash
streamlit run frontend/app.py
```

---

# 📈 Sample Prediction Workflow

```
User Input
      │
      ▼
Streamlit UI
      │
      ▼
FastAPI API
      │
      ▼
Feature Engineering
      │
      ▼
XGBoost Model
      │
      ▼
Predicted Trip Duration
```

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- XGBoost

### Backend

- FastAPI
- Pydantic

### Frontend

- Streamlit

### Model Serialization

- Joblib

# 🔮 Future Improvements

- Integrate real-time traffic information.
- Deploy the application on a cloud platform.
- Add route visualization using interactive maps.
- Improve prediction accuracy through advanced feature engineering.
- Implement automated model retraining.

---

# 👨‍💻 Author

**Mahek Radadiya**

---
