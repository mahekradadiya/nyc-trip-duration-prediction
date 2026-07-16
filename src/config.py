from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

TRAIN_DATA_PATH = RAW_DATA_DIR / "data.csv"

TRAIN_CLEAN_PATH = PROCESSED_DATA_DIR / "data_clean.csv"

TRAIN_PROCESSED_PATH = PROCESSED_DATA_DIR / "data_processed.csv"

MODEL_PATH = BASE_DIR / "models" / "model.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"