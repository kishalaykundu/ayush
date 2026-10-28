"""Test package version and imports."""

import acorn


def test_version():
    """Test that version is defined."""
    assert hasattr(acorn, "__version__")
    assert acorn.__version__ == "0.1.0"


def test_package_imports():
    """Test that package can be imported."""
    assert acorn is not None

