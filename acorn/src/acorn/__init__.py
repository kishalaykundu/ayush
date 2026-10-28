"""Acorn - Ayush HMS Core Package.

This package contains first-class object definitions (dataclass models)
used across Ayush services.

Models are versioned (v1, v2, etc.) for backward compatibility.
The latest stable version is re-exported at the package level.
"""

__version__ = "0.1.0"

# Import current stable version (v1) models
from .models import (
    Department,
    Employee,
    Indian,
    Patient,
    Person,
    Physician,
    User,
)

# Also expose the models module for version-specific imports
from . import models

__all__ = [
    "Department",
    "Employee",
    "Indian",
    "Patient",
    "Person",
    "Physician",
    "User",
    "models",
]

