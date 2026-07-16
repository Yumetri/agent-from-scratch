"""Open a repository command in macOS Terminal.app."""

from __future__ import annotations

import argparse
import platform
import shlex
import subprocess
from pathlib import Path


def applescript_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_shell_command(command: list[str]) -> str:
    root = repository_root()
    quoted_command = " ".join(shlex.quote(part) for part in command)
    return f"cd {shlex.quote(str(root))} && {quoted_command}"


def open_terminal(shell_command: str) -> None:
    if platform.system() != "Darwin":
        raise RuntimeError("open_terminal.py currently supports macOS Terminal.app only.")

    script = "\n".join([
        'tell application "Terminal"',
        "activate",
        f"do script {applescript_string(shell_command)}",
        "end tell",
    ])
    subprocess.run(["osascript", "-e", script], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Open a command in macOS Terminal.app.")
    parser.add_argument("--dry-run", action="store_true", help="Print the shell command without opening Terminal.")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command and arguments to run from the repository root.")
    args = parser.parse_args()
    if not args.command:
        parser.error("command is required")

    shell_command = build_shell_command(args.command)
    if args.dry_run:
        print(shell_command)
        return

    open_terminal(shell_command)


if __name__ == "__main__":
    main()
