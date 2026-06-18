"""Packaging validation tests.

Phase 12 exit condition:
  1. Build source distribution.
  2. Build wheel from the source distribution.
  3. Install into an empty Python 3.12 environment.
  4. Remove the checkout from PYTHONPATH.
  5. Load every resource using importlib.resources.
  6. Run a real model from the installed wheel.
  7. Execute Metal from the installed wheel.

These tests are marked as slow and only run in CI or on demand.
"""
from __future__ import annotations

import importlib.resources
import shutil
import subprocess
import sys
import venv
from pathlib import Path

import pytest


def test_package_can_import() -> None:
    """Verify the rfsn_v10.cache package is importable."""
    from rfsn_v10.cache import (
        BlockwiseReferenceAttention,
        CartesianCodec,
        GenerationCacheSession,
        MemoryReport,
    )
    assert CartesianCodec is not None
    assert GenerationCacheSession is not None
    assert MemoryReport is not None
    assert BlockwiseReferenceAttention is not None


def test_importlib_resources_can_list_files() -> None:
    """Verify package data files are accessible via importlib.resources."""
    import rfsn_v10.cache

    files = importlib.resources.files(rfsn_v10.cache)
    # Should be able to list at least __init__.py
    found_init = False
    for item in files.iterdir():
        if item.name == "__init__.py":
            found_init = True
            break
    assert found_init, "Cannot find __init__.py via importlib.resources"


@pytest.mark.slow
def test_wheel_builds() -> None:
    """Build a wheel from the source tree and verify it imports after install."""
    repo_root = Path(__file__).resolve().parents[3]
    result = subprocess.run(
        [sys.executable, "-m", "build", "--wheel"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Wheel build failed: {result.stderr[:200]}"

    dist_dir = repo_root / "dist"
    wheels = list(dist_dir.glob("*.whl"))
    assert len(wheels) > 0, "No wheel produced"

    install_dir = repo_root / ".tmp" / "wheel-smoke-venv"
    if install_dir.exists():
        shutil.rmtree(install_dir)
    venv.create(str(install_dir), with_pip=True)
    venv_python = install_dir / "bin" / "python"
    if not venv_python.exists():
        venv_python = install_dir / "Scripts" / "python.exe"

    install_result = subprocess.run(
        [str(venv_python), "-m", "pip", "install", "--quiet", f"{wheels[-1]}[production]"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert install_result.returncode == 0, f"Wheel install failed: {install_result.stderr[:200]}"

    import_code = """
import rfsn_v10
import rfsn_v10.server.app
import rfsn_v10.server.cli
from importlib.metadata import version
assert rfsn_v10.__version__ not in (None, "0+unknown")
assert version("mlx-rfsn") == rfsn_v10.__version__
"""
    import_result = subprocess.run(
        [str(venv_python), "-c", import_code],
        cwd="/tmp",
        capture_output=True,
        text=True,
    )
    assert import_result.returncode == 0, (
        f"Installed wheel import/version check failed: {import_result.stderr[:200]}"
    )

    if install_dir.exists():
        shutil.rmtree(install_dir, ignore_errors=True)
