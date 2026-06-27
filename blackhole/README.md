# Black Hole Animation

A zsh wrapper that turns stderr into a black hole consumption animation.

## Usage

```zsh
# Add to ~/.zshrc:
source "$HOME/dev/docker-j/Python/blackhole/bh.zsh"

# Then:
bh <command> [args...]
```

## Examples

```zsh
bh npm test          # Error output gets consumed by a black hole
bh cargo build       # Compilation errors spiral into the void
bh ls /nonexistent   # File not found → sucked in
```

## How It Works

1. `bh` runs your command with stderr/stdout piped
2. As stderr flows, characters spawn and spiral into an animated black hole
3. When the command exits, the animation stops and stdout is printed
4. Uncollected stderr is silently discarded

## Requirements

- macOS (Apple Silicon) with zsh
- Terminal with true color support (24-bit)
- Terminal at least 60 cols × 20 rows

## Architecture

- `bh.zsh` — zsh wrapper function + `BH_SCRIPT` export
- `_bh.py` — Python animation engine (physics + rendering)
- No external dependencies (Python stdlib only)

## Files

```
blackhole/
  bh.zsh              # zsh wrapper (source from .zshrc)
  _bh.py              # Animation engine
  README.md           # This file
```
