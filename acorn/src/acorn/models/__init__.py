"""Data models module.

This module contains all dataclass definitions used across Ayush services.
Models are organized by version (v1, v2, etc.) for backward compatibility.
"""

# Import v1 models (current stable version)
from .v1 import (
    Department,
    Employee,
    Indian,
    Patient,
    Person,
    Physician,
    User,
)

__all__ = [
    "Department",
    "Employee",
    "Indian",
    "Patient",
    "Person",
    "Physician",
    "User",
]

