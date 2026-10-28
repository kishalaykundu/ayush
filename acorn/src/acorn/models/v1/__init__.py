"""Version 1 data models.

This module contains version 1 of all dataclass definitions used across Ayush services.
"""

from .entities import Department
from .patient import Patient
from .person import Indian, Person
from .staff import Employee, Physician
from .user import User

__all__ = [
    "Department",
    "Employee",
    "Indian",
    "Patient",
    "Person",
    "Physician",
    "User",
]

