"""Smoke tests — verify the package imports and exposes its expected metadata.

These tests exist to ensure the CI pipeline runs at least one passing test
from day zero. They will be supplemented with real unit tests as modules are
implemented (see ROADMAP.md).
"""

import actxps_py


def test_package_has_version() -> None:
    """The package exposes a non-empty version string."""
    assert hasattr(actxps_py, "__version__")
    assert isinstance(actxps_py.__version__, str)
    assert len(actxps_py.__version__) > 0


def test_subpackages_importable() -> None:
    """All declared subpackages import cleanly."""
    from actxps_py import (
        credibility,
        data,
        exposure,
        reports,
        study,
        tables,
        viz,
    )

    # Each subpackage should have a docstring describing its role.
    for subpkg in (data, exposure, tables, study, credibility, viz, reports):
        assert subpkg.__doc__ is not None
        assert len(subpkg.__doc__) > 0
