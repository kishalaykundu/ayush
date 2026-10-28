# Contributing to Acorn

Thank you for contributing to the Acorn package!

## Development Setup

1. **Clone and navigate to the package directory:**
   ```bash
   cd /path/to/ayush/acorn
   ```

2. **Install in development mode:**
   ```bash
   make install-dev
   # or
   pip install -e ".[dev]"
   ```

## Creating New Dataclass Models

### Structure

All dataclass models are organized by version in `src/acorn/models/`. The current stable version is `v1`, located in `src/acorn/models/v1/`.

### Example

```python
# src/acorn/models/v1/appointment.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Appointment:
    """Appointment dataclass model."""
    
    id: int
    patient_id: int
    physician_id: int
    scheduled_time: datetime
    duration_minutes: int
    notes: Optional[str] = None
    
    def __post_init__(self) -> None:
        """Validate appointment data."""
        if self.duration_minutes <= 0:
            raise ValueError("duration_minutes must be positive")
        if self.scheduled_time < datetime.now():
            raise ValueError("Cannot schedule appointments in the past")
```

### Exporting Models

After creating a model, export it in the appropriate `__init__.py` files:

1. **In `src/acorn/models/v1/__init__.py`:**
   ```python
   from .appointment import Appointment
   from .patient import Patient
   
   __all__ = ["Appointment", "Patient"]
   ```

2. **In `src/acorn/models/__init__.py`:**
   ```python
   from .v1 import Appointment, Patient
   
   __all__ = ["Appointment", "Patient"]
   ```

3. **In `src/acorn/__init__.py`:**
   ```python
   from .models import Appointment, Patient
   
   __all__ = ["Appointment", "Patient"]
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
from acorn import Patient


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
acorn/
├── src/
│   └── acorn/                     # Main package
│       ├── __init__.py            # Package exports (exports latest stable)
│       ├── py.typed               # Type hints marker
│       └── models/                # Versioned dataclass models
│           ├── __init__.py        # Models exports (exports from latest stable)
│           ├── v1/                # Version 1 models
│           │   ├── __init__.py    # v1 model exports
│           │   ├── entities.py    # Department
│           │   ├── patient.py     # Patient
│           │   ├── person.py      # Person, Indian
│           │   ├── staff.py       # Employee, Physician
│           │   └── user.py        # User
│           └── v2/                # Version 2 models (future)
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

## Model Versioning

Models are organized by version to ensure backward compatibility:

- **v1/**: First stable version of all models
- **v2/**: Future version with breaking changes (when needed)
- The `models/__init__.py` always exports from the latest stable version
- Consumers can import from specific versions for compatibility

### Version Migration Example

```python
# Old code continues to work with version-specific imports
from acorn.models.v1 import Patient

# New code uses the latest version
from acorn import Patient  # Currently points to v1.Patient
```

## Questions?

Contact: Kishalay Kundu <kishalay.kundu@gmail.com>
