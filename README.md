# 🚖 NYC Taxi Trip Duration Prediction

## 📌 Project Overview

The **NYC Taxi Trip Duration Prediction** project estimates the duration of taxi trips in New York City using historical trip records and machine learning techniques. Accurate trip duration prediction can improve route planning, customer experience, fleet management, and operational efficiency for ride-hailing and taxi services.

This project follows a complete end-to-end Machine Learning workflow, from data understanding and preprocessing to feature engineering, model training, evaluation, and deployment using **FastAPI** and **Streamlit**.

---

## 🎯 Problem Statement

Predicting taxi trip duration is a regression problem influenced by several factors, including pickup location, dropoff location, travel distance, pickup time, passenger count, and other trip-related information.

The objective of this project is to build a robust machine learning model capable of accurately predicting taxi trip duration using engineered features derived from the available trip data.

---

## 🎯 Objectives

- Explore and understand the NYC Taxi Trip Duration dataset.
- Perform data cleaning and preprocessing.
- Engineer meaningful features from temporal and geographical information.
- Train and compare multiple regression algorithms.
- Optimize the best-performing model using **RandomizedSearchCV**.
- Evaluate model performance using regression metrics.
- Deploy the trained model using FastAPI.
- Build an interactive Streamlit application for real-time predictions.

---

# 📂 Dataset

This project uses the **NYC Taxi Trip Duration** dataset from Kaggle.

The dataset contains information such as:

- Vendor ID
- Pickup Date & Time
- Pickup Latitude & Longitude
- Dropoff Latitude & Longitude
- Passenger Count
- Store and Forward Flag
- Trip Duration (Target Variable)

### Download Dataset

🔗 https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data?select=train.zip

After downloading, extract the dataset and place **train.csv** inside:

```text
data/raw/
```

---

# 🏗️ Project Structure

```text
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
│   │   └── README.md
│   └── processed/
│       └── README.md
│
├── models/
│   ├── model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_evaluation.ipynb
│
├── src/
│   ├── config.py
│   ├── feature_engineering.py
│   └── __init__.py
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# 🔄 Machine Learning Workflow

```text
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

The following regression algorithms were trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

After comparing all models, the **optimized XGBoost Regressor** achieved the best performance and was selected for deployment.

---

# ⚙️ Feature Engineering

The following features were created during preprocessing:

- Pickup Hour
- Pickup Day
- Pickup Month
- Pickup Weekday
- Pickup Year
- Haversine Distance
- Manhattan Distance
- Bearing
- Encoded Store and Forward Flag

---

# 📊 Model Evaluation

The regression models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# 📈 Results

The optimized **XGBoost Regressor** outperformed the other regression models and was selected as the final model for deployment.

The deployed application predicts taxi trip duration in real time using engineered trip features through a FastAPI backend and an interactive Streamlit interface.

---

# 🚀 Deployment

The project is deployed locally using:

### Backend

- FastAPI

### Frontend

- Streamlit

The Streamlit application collects trip information from the user and sends it to the FastAPI backend. The backend performs feature engineering, loads the trained model, predicts the trip duration, and returns the prediction to the frontend.

---

# 💻 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd NYC_trip_duration
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn backend.app:app --reload
```

FastAPI Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit

```bash
streamlit run frontend/app.py
```

---

# 📈 Prediction Workflow

```text
User Input
      │
      ▼
Streamlit Interface
      │
      ▼
FastAPI Backend
      │
      ▼
Feature Engineering
      │
      ▼
Optimized XGBoost Model
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

### Machine Learning

- Scikit-learn
- XGBoost

### Hyperparameter Tuning

- RandomizedSearchCV

### Backend

- FastAPI
- Pydantic

### Frontend

- Streamlit

### Model Serialization

- Joblib

---

# 🔮 Future Improvements

- Integrate real-time traffic information.
- Deploy the application to a cloud platform.
- Add interactive route visualization.
- Improve prediction accuracy through additional feature engineering.
- Automate model retraining using MLOps practices.

---

# 👨‍💻 Author

**Mahek Radadiya**
