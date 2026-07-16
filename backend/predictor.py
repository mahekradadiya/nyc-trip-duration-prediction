"""
Prediction Module

Loads the trained model and performs predictions
using the same feature engineering pipeline
used during model training.
"""

from pathlib import Path

import joblib
import pandas as pd
import numpy as np

from src.feature_engineering import (
    create_datetime_features,
    haversine_distance,
    manhattan_distance,
    calculate_bearing,
    encode_categorical_features,
    drop_unused_columns
)

# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "model.pkl"
FEATURES_PATH = BASE_DIR / "models" / "feature_columns.pkl"

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)


# ---------------------------------------------------
# Prediction Function
# ---------------------------------------------------

def predict_trip_duration(data: dict) -> float:
    """
    Predict NYC taxi trip duration.

    Parameters
    ----------
    data : dict
        Input data received from FastAPI.

    Returns
    -------
    float
        Predicted trip duration.
    """

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # ------------------------------
    # Feature Engineering
    # ------------------------------

    df = create_datetime_features(df)

    df["haversine_distance"] = haversine_distance(
        df["pickup_latitude"],
        df["pickup_longitude"],
        df["dropoff_latitude"],
        df["dropoff_longitude"]
    )

    df["manhattan_distance"]=manhattan_distance(
        df["pickup_latitude"],
        df["pickup_longitude"],
        df["dropoff_latitude"],
        df["dropoff_longitude"])
    
    df["bearing"]=calculate_bearing(
        df["pickup_latitude"],
        df["pickup_longitude"],
        df["dropoff_latitude"],
        df["dropoff_longitude"]
    )
    
    # Encode categorical variables
    df = encode_categorical_features(df)

    # Remove unused columns
    df = drop_unused_columns(df)

    # ------------------------------
    # Match Training Feature Order
    # ------------------------------

    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # ------------------------------
    # Prediction
    # ------------------------------

    prediction_transformed = model.predict(df)[0]
    prediction = np.expm1(prediction_transformed)

    return float(prediction)