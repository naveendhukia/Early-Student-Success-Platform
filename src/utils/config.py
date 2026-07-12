"""
Configuration loader for the Early Student Success Platform.

Loads:

- .env variables
- config.yaml
- model.yaml

Provides a single Config object that can be imported
throughout the project.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

from src.utils.constants import CONFIG_DIR

# -----------------------------------------------------
# Load environment variables
# -----------------------------------------------------

load_dotenv()


class Config:
    """
    Central configuration loader.
    """

    def __init__(self) -> None:

        self.project = self._load_yaml(CONFIG_DIR / "config.yaml")

        self.models = self._load_yaml(CONFIG_DIR / "model.yaml")

    @staticmethod
    def _load_yaml(path: Path) -> dict[str, Any]:
        """
        Load YAML configuration.

        Parameters
        ----------
        path : Path
            YAML file path.

        Returns
        -------
        dict
            Parsed YAML.
        """

        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


config = Config()
