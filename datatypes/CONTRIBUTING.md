# Contributing to Ayush Datatypes

Thank you for contributing to the Ayush Datatypes package!

## Development Setup

1. **Clone and navigate to the package directory:**
   ```bash
   cd /path/to/ayush/datatypes
   ```

2. **Install in development mode:**
   ```bash
   make install-dev
   # or
   pip install -e ".[dev]"
   ```

## Creating New Dataclass Models

### Structure

All dataclass models should be placed in `src/ayush_datatypes/models/`.

### Example

```python
# src/ayush_datatypes/models/patient.py
from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Patient:
    """Patient dataclass model."""
    
    id: int
    first_name: str
    last_name: str
    date_of_birth: date
    phone: Optional[str] = None
    
    def __post_init__(self) -> None:
        """Validate patient data."""
        if not self.first_name:
            raise ValueError("first_name cannot be empty")
        if not self.last_name:
            raise ValueError("last_name cannot be empty")
    
    @property
    def full_name(self) -> str:
        """Return patient's full name."""
        return f"{self.first_name} {self.last_name}"
```

### Exporting Models

After creating a model, export it in the appropriate `__init__.py` files:

1. **In `src/ayush_datatypes/models/__init__.py`:**
   ```python
   from .patient import Patient
   
   __all__ = ["Patient"]
   ```

2. **In `src/ayush_datatypes/__init__.py`:**
   ```python
   from .models import Patient
   
   __all__ = ["Patient"]
   ```

## Development Workflow

### Running Tests

```bash
make test           # Run all tests
make test-cov       # Run tests with coverage report
```

### Code Quality

```bash
make format         # Format code with ruff
make lint           # Check code style
make type-check     # Run mypy type checker
make all            # Run format, lint, type-check, and test
```

### Before Committing

Always run before committing:
```bash
make all
```

This ensures your code is:
- Properly formatted
- Passes linting checks
- Type-safe
- Passes all tests

## Best Practices

1. **Type Hints**: Always use type hints for all function parameters and return values
2. **Validation**: Add `__post_init__` validation when needed
3. **Documentation**: Add docstrings to all classes and non-trivial methods
4. **Tests**: Write tests for your models in `tests/test_<model_name>.py`
5. **Immutability**: Consider using `frozen=True` for immutable dataclasses

## Example Test

```python
# tests/test_patient.py
from datetime import date
import pytest
from ayush_datatypes import Patient


def test_patient_creation():
    """Test patient creation."""
    patient = Patient(
        id=1,
        first_name="John",
        last_name="Doe",
        date_of_birth=date(1990, 1, 1)
    )
    assert patient.full_name == "John Doe"


def test_patient_validation():
    """Test patient validation."""
    with pytest.raises(ValueError):
        Patient(
            id=1,
            first_name="",
            last_name="Doe",
            date_of_birth=date(1990, 1, 1)
        )
```

## Package Structure

```
datatypes/
├── src/
│   └── ayush_datatypes/          # Main package
│       ├── __init__.py            # Package exports
│       ├── py.typed               # Type hints marker
│       └── models/                # Dataclass models
│           ├── __init__.py        # Models exports
│           └── example.py         # Example model (delete when adding real models)
├── tests/                         # Test suite
│   ├── __init__.py
│   └── test_version.py            # Basic tests
├── pyproject.toml                 # Package configuration
├── Makefile                       # Development commands
├── README.md                      # Package documentation
├── CONTRIBUTING.md                # This file
├── MANIFEST.in                    # Package manifest
├── .gitignore                     # Git ignore rules
└── .editorconfig                  # Editor configuration
```

## Questions?

Contact: Kishalay Kundu <kishalay.kundu@gmail.com>

