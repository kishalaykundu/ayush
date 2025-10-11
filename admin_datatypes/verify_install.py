#!/usr/bin/env python3
"""Verification script to check if the package is properly installed."""

import sys


def verify_installation() -> bool:
    """Verify that the package is properly installed."""
    success = True
    
    print("Verifying admin_datatypes installation...")
    print("-" * 50)
    
    # Test 1: Import package
    try:
        import admin_datatypes
        print("✓ Package import successful")
    except ImportError as e:
        print(f"✗ Package import failed: {e}")
        success = False
        return success
    
    # Test 2: Check version
    try:
        version = admin_datatypes.__version__
        print(f"✓ Version: {version}")
    except AttributeError:
        print("✗ Version attribute not found")
        success = False
    
    # Test 3: Check __all__
    try:
        all_exports = admin_datatypes.__all__
        print(f"✓ Exports (__all__): {all_exports}")
    except AttributeError:
        print("✗ __all__ attribute not found")
        success = False
    
    # Test 4: Check models module
    try:
        from admin_datatypes import models
        print("✓ Models module import successful")
    except ImportError as e:
        print(f"✗ Models module import failed: {e}")
        success = False
    
    # Test 5: Check py.typed marker
    try:
        import admin_datatypes
        import pathlib
        
        package_path = pathlib.Path(admin_datatypes.__file__).parent
        py_typed_path = package_path / "py.typed"
        
        if py_typed_path.exists():
            print("✓ py.typed marker file found")
        else:
            print("✗ py.typed marker file not found")
            success = False
    except Exception as e:
        print(f"✗ py.typed check failed: {e}")
        success = False
    
    print("-" * 50)
    
    if success:
        print("✓ All checks passed!")
        return True
    else:
        print("✗ Some checks failed")
        return False


if __name__ == "__main__":
    success = verify_installation()
    sys.exit(0 if success else 1)

