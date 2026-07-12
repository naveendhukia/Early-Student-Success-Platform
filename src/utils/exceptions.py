"""
Custom exception classes used across the project.
"""


class StudentSuccessException(Exception):
    """
    Base exception for the project.
    """

    def __init__(self, message: str):
        super().__init__(message)


class DataValidationError(StudentSuccessException):
    """Raised when dataset validation fails."""


class DataCleaningError(StudentSuccessException):
    """Raised during data cleaning."""


class FeatureEngineeringError(StudentSuccessException):
    """Raised during feature engineering."""


class ModelTrainingError(StudentSuccessException):
    """Raised when model training fails."""


class PredictionError(StudentSuccessException):
    """Raised during prediction."""


class ConfigurationError(StudentSuccessException):
    """Raised for configuration-related issues."""
