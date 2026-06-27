# Implementation Plan: Black Hole Stderr Animation

## Overview

A zsh wrapper function `bh <command>` that runs the command as a subprocess with piped stderr/stdout. As stderr data streams in, characters immediately spawn and spiral into a black hole animation. When the command exits, the animation stops and buffered stdout is printed. Stderr not yet consumed is silently discarded. Built with Python stdlib only — no external dependencies.

## Architecture Decisions

- **Wrapper approach** (not shell hook): Shell redirections like `2>/dev/null` are processed before command execution, making interception impossible. The `bh` wrapper calls the Python animation engine which runs the command as a subprocess with piped stderr/stdout. Stderr streams into the animation in real-time; stdout is buffered and printed after the animation ends.
- **Single Python file** (`_bh.py`): Animation engine, physics, and rendering all in one file. Modular via classes. Ponytail: no unnecessary splits.
- **True color ANSI rendering**: 24-bit color for smooth fade/darken effects as text approaches the event horizon.
- **Grid-based frame buffer**: Per-frame 2D grid of (char, fg_color) tuples, rendered as a single write call to minimize flicker.
- **30fps target**: Capped delta-time to prevent spiral explosions on frame drops.

## File Structure

```
blackhole/
  bh.zsh              # zsh wrapper + BH_SCRIPT export (sourced from .zshrc)
  _bh.py              # Animation engine: subprocess + real-time stream + physics + rendering
  README.md           # Usage instructions
```

## Task List

### Phase 1: Foundation

- [ ] **Task 1:** Project structure + zsh wrapper + animation skeleton + streaming subprocess
- [ ] **Task 2:** Black hole core rendering + accretion disk + physics

### Checkpoint: Foundation
- [ ] Screen shows animated black hole with spinning accretion disk
- [ ] No text consumption yet — just the hole and disk

### Phase 2: Text Consumption

- [ ] **Task 3:** Streaming text ingestion + character spawning + gravity-driven spiral trajectories
- [ ] **Task 4:** Per-character fade/darken/shadow as text approaches event horizon

### Checkpoint: Core Features
- [ ] Full pipeline: `bh <command>` streams stderr into animation in real-time, stops on exit
- [ ] Text visibly spirals into black hole, fades and darkens on approach
- [ ] Accretion disk continuous, text consumption clean
- [ ] Stdout buffered during animation, printed cleanly after
- [ ] Animation stops immediately when command exits (even if stderr still in queue)

### Phase 3: Polish

- [ ] **Task 5:** Terminal resize handling, clean exit, performance, edge cases

### Checkpoint: Complete
- [ ] All acceptance criteria met
- [ ] `bh echo "hello"`, `bh false`, `bh npm test` all work correctly

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Python too slow for 30fps with many particles | Animation janky | Optimize rendering (batch writes), reduce particle count, cap max frames |
| Terminal doesn't support true color | Faded effects broken | Fallback to 256-color palette; check `$TERM` |
| Terminal too small (< 60 cols) | Animation unusable | Skip animation, just discard stderr silently |
| Binary stderr (non-text) | Garbled animation | Detect binary content, skip animation |
| Signal interrupt during animation | Stuck terminal | SIGINT/SIGTERM handlers restore terminal state |

## Open Questions

- **Accretion disk perspective**: Tilted 3D view (ellipse on screen, more realistic) vs. flat top-down? → **Plan: tilted 3D** (more visually striking, matches real black hole imagery)
- **Max animation duration**: Command might finish before animation completes? → **Plan: animation is command-lifetime bound — stops when command exits, regardless of time**
- **Animation duration cap**: Only if needed as a safety net. → **Plan: 15-second max as hard cutoff**
- **Should animation replay if multiple commands run?** → **Plan: each `bh` invocation is independent**
- **Real-time character spawning**: Characters spawn as stderr arrives (line by line from the pipe), not all at once after command finishes. → **Plan: threaded stderr reader feeds a queue; animation drains it each frame**
