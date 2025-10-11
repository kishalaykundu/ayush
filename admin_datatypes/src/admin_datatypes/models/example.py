"""Example dataclass model.

This is a template file showing how to create dataclass models
in this package. Delete this file when you add your actual models.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ExampleModel:
    """Example dataclass model."""

    id: int
    name: str
    description: Optional[str] = None
    is_active: bool = True

    def __post_init__(self) -> None:
        """Validate the model after initialization."""
        if self.id < 0:
            raise ValueError("id must be non-negative")
        if not self.name:
            raise ValueError("name cannot be empty")

