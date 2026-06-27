# Black hole animation for stderr consumption.
# Add to ~/.zshrc: source "$HOME/dev/docker-j/Python/blackhole/bh.zsh"
# Usage: bh <command> [args...]
# Example: bh npm test

export BH_SCRIPT="$HOME/dev/docker-j/Python/blackhole/_bh.py"

bh() {
    python3 "$BH_SCRIPT" "$@"
}
