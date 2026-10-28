# Model Version Control

This document explains the versioning strategy for Acorn dataclass models.

## Overview

All models in Acorn are versioned to ensure backward compatibility when models evolve. This allows different services to migrate to new model versions at their own pace without breaking existing functionality.

## Directory Structure

```
src/acorn/models/
├── __init__.py          # Exports latest stable version
├── v1/                  # Version 1 (current stable)
│   ├── __init__.py
│   ├── entities.py      # Department
│   ├── patient.py       # Patient
│   ├── person.py        # Person, Indian
│   ├── staff.py         # Employee, Physician
│   └── user.py          # User
└── v2/                  # Version 2 (future)
```

## Current Version: v1

### Available Models

- **Person**: Base person class (abstract)
- **Indian**: Indian person with Aadhaar support
- **Patient**: Patient class extending Indian
- **User**: User class
- **Employee**: Employee base class
- **Physician**: Physician class extending Employee
- **Department**: Department/organizational unit

## Import Patterns

### Pattern 1: Use Latest Stable (Recommended for new code)

```python
from acorn import Patient, Person, Department

# This always imports from the current stable version (v1)
patient = Patient(...)
```

### Pattern 2: Version-Specific Import (For compatibility)

```python
from acorn.models.v1 import Patient, Person
from acorn.models.v2 import Patient as PatientV2  # When v2 exists

# Explicitly use v1
patient_v1 = Patient(...)

# Use v2 when ready
patient_v2 = PatientV2(...)
```

### Pattern 3: Module-Level Import

```python
from acorn.models import v1

# Access all v1 models through the module
patient = v1.Patient(...)
person = v1.Person(...)
```

## When to Create a New Version

Create a new version (v2, v3, etc.) when you need to make **breaking changes** to existing models:

- Renaming fields
- Removing fields
- Changing field types
- Changing validation logic in incompatible ways
- Changing method signatures

## When NOT to Create a New Version

You can modify the current version when making **non-breaking changes**:

- Adding new optional fields (with defaults)
- Adding new methods
- Adding new classes
- Improving documentation
- Fixing bugs in validation

## Creating a New Version

### Step 1: Create Version Directory

```bash
mkdir -p src/acorn/models/v2
```

### Step 2: Copy or Create Models

```bash
# Option A: Start from previous version
cp -r src/acorn/models/v1/* src/acorn/models/v2/

# Option B: Create new models from scratch
touch src/acorn/models/v2/new_model.py
```

### Step 3: Make Your Changes

Edit the v2 models to include your breaking changes.

### Step 4: Create v2/__init__.py

```python
"""Version 2 data models."""

from .patient import Patient
from .person import Person
# ... import other models

__all__ = ["Patient", "Person", ...]
```

### Step 5: Update models/__init__.py

Choose whether v2 becomes the new stable:

```python
# Option A: Keep v1 as stable (recommended initially)
from .v1 import Patient, Person

# Option B: Make v2 the new stable
from .v2 import Patient, Person
```

### Step 6: Update Main Package

Update `src/acorn/__init__.py` to expose the new version:

```python
from .models import v1, v2

# Can also re-export if v2 is now stable
from .models import Patient, Person  # Points to stable version

__all__ = ["Patient", "Person", "v1", "v2"]
```

### Step 7: Document the Changes

- Update CHANGELOG.md with breaking changes
- Update migration guide
- Communicate to consumers

## Version Lifecycle

1. **Development**: Create new version, iterate on changes
2. **Beta**: Test with select consumers
3. **Stable**: Promote to default import path
4. **Deprecated**: Mark old version as deprecated
5. **Removed**: Remove after sufficient migration period (e.g., 1 year)

## Migration Example

### Scenario: Patient model needs a breaking change

**v1 (Current)**
```python
@dataclass
class Patient:
    id: int
    name: str  # Single field
```

**v2 (New)**
```python
@dataclass
class Patient:
    id: int
    first_name: str  # Split into two fields
    last_name: str
```

**Migration Code**
```python
def migrate_patient_v1_to_v2(patient_v1):
    """Migrate Patient from v1 to v2."""
    first, *rest = patient_v1.name.split()
    last = " ".join(rest) if rest else ""
    
    return PatientV2(
        id=patient_v1.id,
        first_name=first,
        last_name=last
    )
```

## Best Practices

1. **Never modify old versions**: Once released, v1 is frozen
2. **Provide migration utilities**: Help consumers upgrade
3. **Document all changes**: Clear changelog and migration guide
4. **Version numbers are sequential**: v1 → v2 → v3 (not v1.1)
5. **Test both versions**: Ensure old and new work independently
6. **Gradual rollout**: Keep old version stable during migration

## Questions?

Contact: Kishalay Kundu <kishalay.kundu@gmail.com>

