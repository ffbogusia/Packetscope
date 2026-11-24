"""Verify that the initial package structure is importable."""

from importlib import import_module


def test_project_packages_import() -> None:
    """Import the application and each reserved package."""
    for name in ("app", "app.parser", "app.detection", "app.models", "app.reporting"):
        module = import_module(name)
        assert module.__name__ == name
