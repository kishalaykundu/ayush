"""Test package version and imports."""

import admin_datatypes


def test_version():
    """Test that version is defined."""
    assert hasattr(admin_datatypes, "__version__")
    assert admin_datatypes.__version__ == "0.1.0"


def test_package_imports():
    """Test that package can be imported."""
    assert admin_datatypes is not None

