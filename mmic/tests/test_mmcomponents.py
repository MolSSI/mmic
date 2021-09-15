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


def test_mmic_strategy():
    class Foo(mmic.components.blueprints.strategy_component.StrategyComponent):
        @classmethod
        def input(cls):
            return {}

        @classmethod
        def output(cls):
            return {}

        @classmethod
        def get_version(cls):
            return ""

        @classmethod
        def tactic_comps(cls):
            return set()

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
    class Foo(mmic.components.blueprints.tactic_component.TacticComponent):
        @classmethod
        def input(cls):
            return {}

        @classmethod
        def output(cls):
            return {}

        @classmethod
        def get_version(cls):
            return ""

        @classmethod
        def strategy_comps(cls):
            return ""

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
