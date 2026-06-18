"""Version lookup for the MLX-RFSN package.

The project no longer depends on a generated ``_version.py`` file. Installed
wheels report the version through package metadata, while source-tree imports
fall back to the single static version in ``pyproject.toml``.
"""

from __future__ import annotations

import importlib.metadata
from pathlib import Path


def get_package_version() -> str:
    """Return the MLX-RFSN package version."""
    try:
        return importlib.metadata.version("mlx-rfsn")
    except importlib.metadata.PackageNotFoundError:
        pass

    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    if pyproject.exists():
        try:
            import tomllib
        except ImportError:  # pragma: no cover - Python 3.10 fallback
            import tomli as tomllib

        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        version = data.get("project", {}).get("version")
        if isinstance(version, str) and version:
            return version

    return "0+unknown"


__version__ = get_package_version()
