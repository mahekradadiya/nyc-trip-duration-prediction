"""
Pydantic Schemas

Defines the request and response models for the NYC Taxi
Trip Duration Prediction API.
"""

from datetime import datetime
from pydantic import BaseModel, Field


class TripData(BaseModel):
    """
    Input schema for trip prediction.
    """

    vendor_id: int = Field(
        ...,
        ge=1,
        le=2,
        description="Vendor ID (1 or 2)"
    )

    passenger_count: int = Field(
        ...,
        ge=1,
        le=6,
        description="Number of passengers (1-6)"
    )

    pickup_datetime: datetime = Field(
        ...,
        description="Pickup datetime (YYYY-MM-DD HH:MM:SS)"
    )

    pickup_longitude: float = Field(
        ...,
        ge=-74.3,
        le=-73.6,
        description="Pickup longitude"
    )

    pickup_latitude: float = Field(
        ...,
        ge=40.5,
        le=41.0,
        description="Pickup latitude"
    )

    dropoff_longitude: float = Field(
        ...,
        ge=-74.3,
        le=-73.6,
        description="Dropoff longitude"
    )

    dropoff_latitude: float = Field(
        ...,
        ge=40.5,
        le=41.0,
        description="Dropoff latitude"
    )

    store_and_fwd_flag: str = Field(
        ...,
        pattern="^[YN]$",
        description="Store and Forward Flag (Y or N)"
    )


class PredictionResponse(BaseModel):
    """
    Response schema.
    """

    predicted_trip_duration: float