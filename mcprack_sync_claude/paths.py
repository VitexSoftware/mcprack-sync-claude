"""Resolve Claude Desktop / Claude Code MCP config paths."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _home() -> Path:
    return Path.home()


def claude_desktop_config_path() -> Path:
    if sys.platform == "darwin":
        return _home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", str(_home() / "AppData" / "Roaming"))
        return Path(appdata) / "Claude" / "claude_desktop_config.json"
    # Linux / other XDG
    xdg = os.environ.get("XDG_CONFIG_HOME", str(_home() / ".config"))
    return Path(xdg) / "Claude" / "claude_desktop_config.json"


def claude_code_config_path() -> Path:
    return _home() / ".claude.json"
