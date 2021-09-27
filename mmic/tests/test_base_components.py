"""
Unit and regression test for the mmic package.
"""

# Import package, test suite, and other packages as needed
import mmic
import sys


def test_mmic_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic" in sys.modules


def test_mmic_program():

    Foo = type(
        "Foo",
        (mmic.components.base.base_component.ProgramHarness,),
        {
            "version": lambda: ...,
            "input": lambda: ...,
            "output": lambda: ...,
            "found": lambda: ...,
            "execute": lambda: ...,
        },
    )

    f = Foo(
        name="foo",
        scratch=False,
        thread_safe=False,
        thread_parallel=False,
        node_parallel=False,
        managed_memory=False,
        extras=None,
    )
