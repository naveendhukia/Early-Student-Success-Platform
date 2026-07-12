"""
Centralized logging configuration for the Early Student Success Platform.

This module exposes a project-wide Loguru logger that writes logs to both
the console and rotating log files.

Example:
    from src.utils.logger import logger

    logger.info("Training started...")
"""

from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger

from src.utils.constants import LOG_DIR

# ---------------------------------------------------------------------
# Ensure log directory exists
# ---------------------------------------------------------------------

LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = Path(LOG_DIR) / "platform.log"

# ---------------------------------------------------------------------
# Remove default logger
# ---------------------------------------------------------------------

logger.remove()

# ---------------------------------------------------------------------
# Console Logger
# ---------------------------------------------------------------------

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> "
        "- <level>{message}</level>"
    ),
)

# ---------------------------------------------------------------------
# File Logger
# ---------------------------------------------------------------------

logger.add(
    LOG_FILE,
    level="DEBUG",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    encoding="utf-8",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{name}:{function}:{line} | "
        "{message}"
    ),
)

__all__ = ["logger"]
