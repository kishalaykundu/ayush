"""Test package version and imports."""

import ayush_datatypes


def test_version():
    """Test that version is defined."""
    assert hasattr(ayush_datatypes, "__version__")
    assert ayush_datatypes.__version__ == "0.1.0"


def test_package_imports():
    """Test that package can be imported."""
    assert ayush_datatypes is not None

