"""
Global constants used throughout the project.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ------------------------------------------------------------------
# Directory Paths
# ------------------------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"

MODEL_DIR = PROJECT_ROOT / "models"

ARTIFACT_DIR = PROJECT_ROOT / "artifacts"

LOG_DIR = PROJECT_ROOT / "logs"

MLFLOW_DIR = PROJECT_ROOT / "mlruns"

CONFIG_DIR = PROJECT_ROOT / "configs"

TEST_DIR = PROJECT_ROOT / "tests"

# ------------------------------------------------------------------
# Dataset
# ------------------------------------------------------------------

DATASET_FILENAME = "student_dropout.csv"

# ------------------------------------------------------------------
# Model Files
# ------------------------------------------------------------------

MODEL_FILE = MODEL_DIR / "best_model.joblib"

PREPROCESSOR_FILE = MODEL_DIR / "preprocessor.joblib"

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------

LOG_FILE = LOG_DIR / "platform.log"

# ------------------------------------------------------------------
# Random State
# ------------------------------------------------------------------

RANDOM_STATE = 42

# ------------------------------------------------------------------
# Train/Test Split
# ------------------------------------------------------------------

TEST_SIZE = 0.20

VALIDATION_SIZE = 0.20
