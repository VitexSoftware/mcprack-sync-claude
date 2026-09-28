from __future__ import annotations

import sys

from mcprack_client.cli import run_cli

from .paths import claude_code_config_path, claude_desktop_config_path


def main(argv: list[str] | None = None) -> int:
    argv_list = list(sys.argv[1:] if argv is None else argv)
    use_code = False
    filtered: list[str] = []
    for arg in argv_list:
        if arg in ("--claude-code", "--code"):
            use_code = True
            continue
        filtered.append(arg)

    resolve = claude_code_config_path if use_code else claude_desktop_config_path
    return run_cli(
        prog="mcprack-sync-claude",
        description=(
            "Keep Claude Desktop MCP config in sync with mcprack. "
            "Pass --claude-code to target ~/.claude.json instead."
        ),
        tool="claude-code" if use_code else "claude-desktop",
        api_client="claude",
        servers_key="mcpServers",
        resolve_config_path=resolve,
        argv=filtered,
    )


if __name__ == "__main__":
    raise SystemExit(main())
