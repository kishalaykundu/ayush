# Acorn

Core package of the Ayush HMS (Hospital Management System). Contains first-class object definitions (dataclass models) used by Ayush services.

## Installation

### From Source

```bash
pip install -e .
```

### For Development

```bash
pip install -e ".[dev]"
```

## Usage

### Basic Usage (Latest Stable Version)

```python
# Import models from the latest stable version (currently v1)
from acorn import Patient, Person, Department, Employee, Physician, User

# Use your dataclass models
patient = Patient(...)
```

### Version-Specific Imports

```python
# Import from a specific version for backward compatibility
from acorn.models.v1 import Patient, Person
from acorn.models.v2 import NewModel  # When v2 is available

# Or access all models from a version
from acorn.models import v1, v2
patient_v1 = v1.Patient(...)
patient_v2 = v2.Patient(...)  # When v2 is available
```

## Package Structure

```
acorn/
├── src/
│   └── acorn/
│       ├── __init__.py        # Package initialization & exports
│       ├── py.typed           # PEP 561 marker for type hints
│       └── models/            # Versioned dataclass models
│           ├── __init__.py    # Exports latest stable version
│           ├── v1/            # Version 1 models
│           │   ├── __init__.py
│           │   ├── entities.py
│           │   ├── patient.py
│           │   ├── person.py
│           │   ├── staff.py
│           │   └── user.py
│           └── v2/            # Version 2 models (future)
├── tests/                     # Unit tests
├── pyproject.toml            # Package configuration
└── README.md                 # This file
```

## Development

### Adding New Models to Current Version (v1)

1. Create your dataclass model in `src/acorn/models/v1/your_model.py`
2. Import it in `src/acorn/models/v1/__init__.py` and add to `__all__`
3. Import it in `src/acorn/models/__init__.py` and add to `__all__`
4. Import it in `src/acorn/__init__.py` and add to `__all__`

### Creating a New Version (v2, v3, etc.)

1. Create a new version directory: `src/acorn/models/v2/`
2. Copy models from previous version or create new ones
3. Create `src/acorn/models/v2/__init__.py` with exports
4. Update `src/acorn/models/__init__.py` to import from the new version
5. Update `src/acorn/__init__.py` to export the new stable version

### Running Tests

```bash
pytest
```

## Requirements

- Python 3.13
- phonenumbers >= 9, < 10

## License

See the LICENSE file in the parent project.

## Authors

- Kishalay Kundu <kishalay.kundu@gmail.com>
