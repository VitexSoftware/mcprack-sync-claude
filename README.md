# mcprack-sync-claude

Keep **Claude Desktop** (and optionally **Claude Code**) MCP server configuration
up to date from a [mcprack](https://github.com/VitexSoftware/mcprack) catalog.

## Install

```bash
sudo apt install mcprack-sync-claude
# or from source (with mcprack-client on PYTHONPATH / installed):
pip install .
```

## One-time setup

1. In mcprack, create a personal API token (user menu → API tokens).
2. Configure the sync tool:

```bash
mcprack-sync-claude configure \
  --url https://mcprack.example.com \
  --token mcr_your_token_here
```

Settings are stored in `~/.config/mcprack/client.env` (shared with the Cursor and VS Code sync tools).

## Sync

```bash
mcprack-sync-claude sync              # Claude Desktop
mcprack-sync-claude sync --dry-run
mcprack-sync-claude sync --claude-code   # merge into ~/.claude.json
mcprack-sync-claude status
```

Default target (Linux): `~/.config/Claude/claude_desktop_config.json`

Only the `mcpServers` key is updated. Other top-level keys (preferences, etc.)
and local-only servers that were never managed by mcprack are preserved.

## Automatic updates

Enable the systemd user timer:

```bash
systemctl --user enable --now mcprack-sync-claude.timer
```

## License

MIT
