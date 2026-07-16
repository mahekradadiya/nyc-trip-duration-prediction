import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def create_datetime_features(df):
    """
    Create datetime-based features from dropoff_datetime.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    df = df.copy()

    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])

    df["dropoff_month"] = df["dropoff_datetime"].dt.month
    df["dropoff_day"] = df["dropoff_datetime"].dt.day
    df["dropoff_weekday"] = df["dropoff_datetime"].dt.weekday
    df["dropoff_hour"] = df["dropoff_datetime"].dt.hour
    df["dropoff_minute"] = df["dropoff_datetime"].dt.minute

    df["is_weekend"] = (
        df["dropoff_weekday"]
        .isin([5, 6])
        .astype(int)
    )

    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

    df["pickup_month"] = df["pickup_datetime"].dt.month
    df["pickup_day"] = df["pickup_datetime"].dt.day
    df["pickup_weekday"] = df["pickup_datetime"].dt.weekday
    df["pickup_hour"] = df["pickup_datetime"].dt.hour
    df["pickup_minute"] = df["pickup_datetime"].dt.minute

    df["is_weekend"] = (
        df["pickup_weekday"]
        .isin([5, 6])
        .astype(int)
    )
    return df

# haversine distance

def haversine_distance(lat1, lon1, lat2, lon2):

    R = 6371.0

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

# manhattan distance

def manhattan_distance(lat1, lon1, lat2, lon2):

        return (
        np.abs(lat2 - lat1)
        + np.abs(lon2 - lon1)
    )

# bearing

from math import radians, sin, cos, sqrt, asin,degrees,atan2
def calculate_bearing(lat1, lon1, lat2, lon2):

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlon = lon2 - lon1

    x = np.sin(dlon) * np.cos(lat2)

    y = (
        np.cos(lat1) * np.sin(lat2)
        - np.sin(lat1)
        * np.cos(lat2)
        * np.cos(dlon)
    )

    bearing = np.degrees(np.arctan2(x, y))

    return (bearing + 360) % 360

# encode column

def encode_categorical_features(df):
    """
    Encode categorical features into numerical values.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    df = df.copy()

    # Store and Forward Flag
    df["store_and_fwd_flag"] = df["store_and_fwd_flag"].map({
        "N": 0,
        "Y": 1
    })

    return df

# drop column

def drop_unused_columns(df):

    """
    Drop columns that are not required for model training.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    df = df.copy()

    columns_to_drop = [
        "id",
        "vendor_id",
        "pickup_datetime",
        "dropoff_datetime"
    ]

    df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

    return df

def evaluate_model(model_name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    print(f"\n{model_name}")
    print("-" * 40)
    print(f"MAE  : {mae}")
    print(f"MSE  : {mse}")
    print(f"RMSE : {rmse}")
    print(f"R²   : {r2}")

    return mae, mse, rmse, r2
