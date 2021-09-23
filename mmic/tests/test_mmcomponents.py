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

    Foo = type(
        "Foo", (mmic.components.blueprints.GenericComponent,), {"execute": lambda: ...}
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


def test_mmic_strategy():
    Foo = type(
        "Foo",
        (mmic.components.blueprints.StrategyComponent,),
        {
            "version": lambda: "",
            "tactic_comps": lambda: set(),
            "input": lambda: {},
            "output": lambda: {},
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


def test_mmic_tactic():
    Foo = type(
        "Foo",
        (mmic.components.blueprints.TacticComponent,),
        {
            "version": lambda: "",
            "strategy_comps": lambda: set(),
            "input": lambda: {},
            "output": lambda: {},
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
