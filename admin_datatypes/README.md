# Admin Datatypes

Admin package of the Ayush HMS (Hospital Management System). Contains first-class object definitions (dataclass models) used by Ayush admin services.

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

```python
from admin_datatypes import YourModel

# Use your dataclass models
```

## Package Structure

```
admin_datatypes/
├── src/
│   └── admin_datatypes/
│       ├── __init__.py        # Package initialization
│       ├── py.typed           # PEP 561 marker for type hints
│       └── models/            # Your dataclass models go here
├── tests/                     # Unit tests
├── pyproject.toml            # Package configuration
└── README.md                 # This file
```

## Development

### Adding New Models

1. Create your dataclass models in `src/admin_datatypes/models/`
2. Import them in `src/admin_datatypes/__init__.py`
3. Add them to `__all__` for proper exports

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

