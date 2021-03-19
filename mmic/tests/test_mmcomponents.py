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


def test_mmic_generic():
    class Foo(mmic.components.blueprints.generic_component.GenericComponent):
        def execute(self):
            pass

    f = Foo(
        name="foo",
        scratch=False,
        thread_safe=False,
        thread_parallel=False,
        node_parallel=False,
        managed_memory=False,
        extras=None,
    )


def test_mmic_validation():
    class Foo(mmic.components.blueprints.generic_component.GenericComponent):
        def execute(self, inputs):
            return True, self.output()()
