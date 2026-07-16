"""
FastAPI Application

This module exposes REST API endpoints for
NYC Taxi Trip Duration Prediction.
"""

from fastapi import FastAPI

from backend.schemas import (
    TripData,
    PredictionResponse
)

from backend.predictor import predict_trip_duration


# -------------------------------------------------------
# Create FastAPI Application
# -------------------------------------------------------

app = FastAPI(
    title="NYC Taxi Trip Duration Prediction API",
    description="Predict NYC taxi trip duration using a trained XGBoost model.",
    version="1.0.0"
)


# -------------------------------------------------------
# Root Endpoint
# -------------------------------------------------------

@app.get("/")
def home():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to NYC Taxi Trip Duration Prediction API 🚖"
    }


# -------------------------------------------------------
# Health Check Endpoint
# -------------------------------------------------------

@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "API is running successfully"
    }


# -------------------------------------------------------
# Prediction Endpoint
# -------------------------------------------------------

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(data: TripData):
    """
    Predict taxi trip duration.
    """

    prediction = predict_trip_duration(
        data.model_dump()
    )

    return PredictionResponse(
        predicted_trip_duration=round(prediction, 2)
    )