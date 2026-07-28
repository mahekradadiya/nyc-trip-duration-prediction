"""
Streamlit Frontend

This application provides a user-friendly interface
for predicting NYC taxi trip duration using the
FastAPI backend.
"""
import streamlit_datetime_picker
from datetime import datetime
import streamlit as st
import requests

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="NYC Taxi Trip Duration Prediction",
    page_icon="🚖",
    layout="centered"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🚖 NYC Taxi Trip Duration Prediction")

st.markdown("""
Predict the duration of an NYC taxi trip using a trained
Machine Learning model powered by **FastAPI** and **XGBoost**.
""")

st.divider()

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

st.subheader("Trip Details")

vendor_id = st.selectbox(
    "Vendor ID",
    [1, 2]
)

passenger_count = st.number_input(
    "Passenger Count",
    min_value=1,
    max_value=6,
    value=1
)

col1, col2 = st.columns([2, 1])

with col1:
    pickup_date = st.date_input("Pickup Date")

with col2:
    pickup_time = st.time_input("Pickup Time")

pickup_datetime = datetime.combine(pickup_date, pickup_time)

pickup_longitude = st.number_input(
    "Pickup Longitude",
    value=-73.982154,
    format="%.6f"
)

pickup_latitude = st.number_input(
    "Pickup Latitude",
    value=40.767937,
    format="%.6f"
)

dropoff_longitude = st.number_input(
    "Dropoff Longitude",
    value=-73.964630,
    format="%.6f"
)

dropoff_latitude = st.number_input(
    "Dropoff Latitude",
    value=40.765602,
    format="%.6f"
)

store_and_fwd_flag = st.selectbox(
    "Store and Forward Flag",
    ["N", "Y"]
)

# --------------------------------------------------
# Predict Button
# --------------------------------------------------

if st.button("Predict Trip Duration"):

    payload = {

        "vendor_id": vendor_id,

        "passenger_count": passenger_count,

        "pickup_datetime": pickup_datetime.isoformat(),

        "pickup_longitude": pickup_longitude,

        "pickup_latitude": pickup_latitude,

        "dropoff_longitude": dropoff_longitude,

        "dropoff_latitude": dropoff_latitude,

        "store_and_fwd_flag": store_and_fwd_flag

    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:

            prediction = response.json()["predicted_trip_duration"]

            st.success(
                f"🚖 Estimated Trip Duration: **{prediction:.2f} seconds**"
            )

            st.info(
                f"Approximate Duration: **{prediction/60:.2f} minutes**"
            )

        else:

            st.error("Prediction failed.")

            st.write(response.json())

    except Exception as e:

        st.error("Unable to connect to FastAPI server.")

        st.exception(e)