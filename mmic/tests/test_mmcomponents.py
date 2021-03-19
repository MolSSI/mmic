"""
Unit and regression test for the mmic package.
"""

# Import package, test suite, and other packages as needed
import mmic
import pytest
import sys


def test_mmic_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic" in sys.modules
