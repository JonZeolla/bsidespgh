#!/usr/bin/env python3
"""
Test main.py module
"""

import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest


@pytest.mark.unit
def test_main_import():
    """Test that main.py can be imported without executing"""
    import main  # noqa: F401


@pytest.mark.unit
def test_main_function():
    """Test that main() shows help when called with no args"""
    from main import main

    # Mock sys.argv to simulate no arguments
    with patch("sys.argv", ["main.py"]):
        # Capture the output
        with patch("builtins.print") as mock_print:
            main()

            # Check that help was shown
            print_calls = [str(call) for call in mock_print.call_args_list]
            assert any("--vibe" in str(call) for call in print_calls)
            assert any("Tip:" in str(call) for call in print_calls)


@pytest.mark.unit
def test_main_as_script():
    """Test that main.py shows help when run as a script with no args"""
    main_path = Path(__file__).parent.parent / "src" / "main.py"

    result = subprocess.run(
        [sys.executable, str(main_path)],
        capture_output=True,
        text=True,
    )

    # Should exit successfully
    assert result.returncode == 0
    # Should show help text
    assert "--vibe" in result.stdout
    assert "Tip:" in result.stdout
