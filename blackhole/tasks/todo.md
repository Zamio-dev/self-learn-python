# Black Hole Animation — Task Checklist

## Phase 1: Foundation

- [x] **Task 1:** Project structure + zsh wrapper + streaming animation skeleton
  - Files: `bh.zsh`, `_bh.py` (skeleton), `README.md`
  - zsh wrapper: `bh() { python3 "$BH_SCRIPT" "$@"; }` + `export BH_SCRIPT=...`
  - Python: subprocess with piped stdout/stderr, threaded stderr reader → queue
  - Python: terminal detection, frame loop (30fps), rendering infrastructure (grid buffer, ANSI output)
  - Streaming: stderr reader thread drains subprocess pipe into a queue; animation loop drains queue each frame
  - Verification: `python3 _bh.py true` runs black screen with no errors (no stderr → no animation triggers)

- [x] **Task 2:** Black hole core rendering + accretion disk + physics
  - Files: `_bh.py` (extend)
  - Event horizon (pure void, matches terminal background)
  - Photon sphere (bright ring at 1.5× event horizon radius)
  - Accretion disk particle system (~100 particles, orbital mechanics)
  - Keplerian orbital speeds (inner faster than outer)
  - Doppler shift coloring (blueshift/redshift based on velocity direction)
  - Gravitational redshift (inner particles brighter/hotter)
  - Time dilation on accretion particles near horizon
  - Verification: animated black hole with spinning, color-shifting accretion disk

## Checkpoint: Foundation
- [ ] Screen shows animated black hole with spinning accretion disk
- [ ] No text consumption yet — just the hole and disk
- [ ] `python3 _bh.py true` runs cleanly (no stderr → no animation text, just hole + disk)

## Phase 2: Text Consumption

- [x] **Task 3:** Streaming text ingestion + character spawning + gravity-driven spiral trajectories
  - Files: `_bh.py` (extend)
  - Threaded stderr reader feeds data into a queue as it arrives from subprocess
  - Animation loop drains queue each frame: each chunk → individual characters
  - Characters spawn at random screen edges with initial velocity (toward center + tangential)
  - Newtonian gravity + tangential velocity → spiral trajectories
  - Gravitational lensing tangential deflection near photon sphere
  - Event horizon collision detection (character removed when consumed)
  - Characters that haven't been fed yet simply don't exist in the simulation
  - Verification: run `bh sh -c 'for i in 1 2 3 4 5; do echo "error_$i"; sleep 0.3; done'` — characters appear and spiral in as each line arrives

- [x] **Task 4:** Per-character fade/darken/shadow as text approaches event horizon
  - Files: `_bh.py` (extend)
  - Proximity-based opacity: full opacity far away → transparent at horizon
  - Proximity-based darkening: original color → darker → black at horizon
  - Shadow effect: darker + faded = "sucked into void" look
  - Characters shrink slightly as they approach (gravitational lensing feel)
  - Time dilation: characters visibly slow down near horizon
  - Multi-line stderr handled (newlines replaced with spaces, chars distributed across edges)
  - Verification: text visibly fades and darkens as it gets consumed

## Checkpoint: Core Features
- [ ] Full pipeline: `bh <command>` streams stderr into animation in real-time, stops on exit
- [ ] Stdout buffered during animation, printed cleanly after command exits
- [ ] Text spirals in, fades, darkens, vanishes at horizon
- [ ] Accretion disk continues spinning throughout
- [ ] Animation stops immediately when command exits (even if stderr queue has remaining data)
- [ ] Uncollected stderr silently discarded

## Phase 3: Polish

- [x] **Task 5:** Terminal resize, clean exit, performance, edge cases
  - Files: `_bh.py` (extend)
  - Handle SIGWINCH (terminal resize) — recalculate positions, no reset
  - Handle SIGINT/SIGTERM — restore terminal, kill subprocess, print buffered stdout
  - Minimum terminal size check (skip animation if < 60 cols or < 20 rows)
  - Binary stderr detection (skip animation gracefully)
  - Hard animation cutoff: 15 seconds max (safety net)
  - Performance: batch ANSI writes, minimize flicker
  - Verification: `bh echo "test"`, `bh false`, `bh ls /nonexistent`, `bh sh -c 'sleep 0.1; echo err'` all work

## Checkpoint: Complete
- [ ] All acceptance criteria met
- [ ] Ready for review
