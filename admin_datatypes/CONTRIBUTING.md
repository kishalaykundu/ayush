# Contributing to Admin Datatypes

Thank you for contributing to the Admin Datatypes package!

## Development Setup

1. **Clone and navigate to the package directory:**
   ```bash
   cd /path/to/ayush/admin_datatypes
   ```

2. **Install in development mode:**
   ```bash
   make install-dev
   # or
   pip install -e ".[dev]"
   ```

## Creating New Dataclass Models

### Structure

All dataclass models should be placed in `src/admin_datatypes/models/`.

### Example

```python
# src/admin_datatypes/models/admin.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Admin:
    """Admin user dataclass model."""
    
    id: int
    username: str
    email: str
    role: str
    created_at: datetime
    is_active: bool = True
    
    def __post_init__(self) -> None:
        """Validate admin data."""
        if not self.username:
            raise ValueError("username cannot be empty")
        if not self.email:
            raise ValueError("email cannot be empty")
        if "@" not in self.email:
            raise ValueError("invalid email format")
```

### Exporting Models

After creating a model, export it in the appropriate `__init__.py` files:

1. **In `src/admin_datatypes/models/__init__.py`:**
   ```python
   from .admin import Admin
   
   __all__ = ["Admin"]
   ```

2. **In `src/admin_datatypes/__init__.py`:**
   ```python
   from .models import Admin
   
   __all__ = ["Admin"]
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
# tests/test_admin.py
from datetime import datetime
import pytest
from admin_datatypes import Admin


def test_admin_creation():
    """Test admin creation."""
    admin = Admin(
        id=1,
        username="admin",
        email="admin@example.com",
        role="superuser",
        created_at=datetime.now()
    )
    assert admin.username == "admin"
    assert admin.is_active is True


def test_admin_validation():
    """Test admin validation."""
    with pytest.raises(ValueError):
        Admin(
            id=1,
            username="",
            email="admin@example.com",
            role="superuser",
            created_at=datetime.now()
        )
```

## Package Structure

```
admin_datatypes/
├── src/
│   └── admin_datatypes/           # Main package
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

