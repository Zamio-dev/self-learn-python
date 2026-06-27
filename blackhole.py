#!/usr/bin/env python3
"""Terminal blackhole — particles spiral in, redshift, cross event horizon."""

import math, random, time, os, sys, signal

try:
    W, H = os.get_terminal_size().columns - 2, 28
except OSError:
    W, H = 100, 28
CX, CY = W // 2, H // 2
R_H = 4            # event horizon
R_ISCO = 12        # innermost stable orbit ring
R_ACCRETION = 35   # accretion disk outer edge
GM = 18            # gravitational constant * mass
NUM = 280

sys.stdout.write("\033[H\033[2J")
sys.stdout.flush()
signal.signal(signal.SIGALRM, lambda s, f: sys.exit())

SYMBOLS = list("·•●░▒▓█♪♫∑≈∞◆◇○□△▽☆⊕⊗⊘⊙")


def spawn():
    """Spawn a particle on a random elliptical orbit."""
    r = random.uniform(R_ISCO + 2, max(R_ACCRETION, min(W, H) * 0.45))
    a = random.uniform(0, 2 * math.pi)
    # Near-circular orbital velocity (Keplerian)
    v_circ = math.sqrt(GM / max(r - 1, 1)) * random.uniform(0.7, 1.1)
    # Random slight eccentricity
    v_r = v_circ * random.uniform(-0.2, 0.2)
    vx = -v_circ * math.sin(a) + v_r * math.cos(a)
    vy = v_circ * math.cos(a) * 0.65 + v_r * math.sin(a) * 0.65
    return {
        "x": CX + r * math.cos(a),
        "y": CY + r * math.sin(a) * 0.7,
        "vx": vx,
        "vy": vy,
        "sym": SYMBOLS[random.randint(0, len(SYMBOLS) - 1)],
        "age": 0,
    }


particles = [spawn() for _ in range(NUM)]

while True:
    grid = [[" "] * W for _ in range(H)]
    dt = 1.0  # timestep units

    for p in particles:
        dx = p["x"] - CX
        dy = p["y"] - CY
        dist = math.sqrt(dx * dx + dy * dy)
        if dist < 0.3:
            dist = 0.3

        # Schwarzschild-inspired gravity: stronger near horizon
        # Newtonian with relativistic correction term
        r_rel = max(dist - 1.5, 0.3)  # softening
        accel = GM / (r_rel * r_rel)  # 1/r²
        # Extra pull near event horizon (photon sphere effect)
        if dist < R_ISCO + 4:
            accel *= 1.0 + 6.0 / (dist * dist)

        p["vx"] -= accel * dx / dist * 0.018 * dt
        p["vy"] -= accel * dy / dist * 0.018 * dt

        # Frame-dragging (Lense-Thirring) — tangential push
        # Simulates rotating spacetime dragging particles
        drag = 0.15 / (dist * dist + 2)
        p["vx"] += -dy / dist * drag * 0.012 * dt
        p["vy"] += dx / dist * drag * 0.012 * dt

        # Small inward drift (gravitational wave energy loss)
        if dist > R_ISCO:
            p["vx"] -= dx / dist * 0.001 * dt
            p["vy"] -= dy / dist * 0.001 * dt

        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["age"] += 1

        # Absorbed by event horizon
        if dist < R_H:
            np = spawn()
            # Bias spawn direction opposite to last absorption for variety
            np["x"] = CX + random.uniform(-R_ACCRETION * 0.5, R_ACCRETION * 0.5)
            np["y"] = CY + random.uniform(-R_ACCRETION * 0.35, R_ACCRETION * 0.35)
            idx = particles.index(p)
            particles[idx] = np
            continue

        ix = int(p["x"])
        iy = int(p["y"])
        if not (0 <= ix < W and 0 <= iy < H):
            np = spawn()
            idx = particles.index(p)
            particles[idx] = np
            continue

        # --- Color based on physics ---
        speed = math.sqrt(p["vx"] ** 2 + p["vy"] ** 2)
        v_factor = min(speed * 2.5, 1.0)  # 0..1 normalized

        if dist < R_H + 2:
            color = "\033[38;5;255m"        # near-white (spaghettification heat)
        elif dist < R_ISCO:
            # Deep in gravity well — extreme blueshift + thermal
            t = int(230 + 25 * v_factor)     # 230–255 (near-white)
            color = f"\033[38;5;{t}m"
        elif dist < R_ISCO + 6:
            # Hot accretion: blue-white → white → yellow
            if v_factor > 0.6:
                t = int(15 + 60 * v_factor)  # 15–75 (blue → cyan)
            else:
                t = int(20 + 40 * (1 - v_factor))  # warmer slow particles
            color = f"\033[38;5;{max(0, min(255, t))}m"
        elif dist < R_ACCRETION * 0.6:
            # Medium: orange → red based on speed (Doppler)
            t = int(196 + 40 * v_factor)
            color = f"\033[38;5;{max(0, min(255, t))}m"
        else:
            # Cold outer: dim reds and grays
            t = int(88 + 50 * v_factor)
            color = f"\033[38;5;{max(0, min(255, t))}m"

        # Symbol flicker based on speed (faster = more chaotic)
        if speed > 2.5 and random.random() < 0.3:
            sym = SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
        else:
            sym = p["sym"]

        # Brightness hint: fast particles brighter (white-inset)
        if speed > 3:
            sym = f"\033[1m{sym}"

        grid[iy][ix] = f"{color}{sym}\033[0m"

    # --- Event horizon ---
    # Render as black circle with subtle edge glow
    for dy in range(-R_H - 1, R_H + 2):
        for dx in range(-R_H - 1, R_H + 2):
            d = math.sqrt(dx * dx + dy * dy)
            px, py = CX + dx, CY + dy
            if not (0 <= px < W and 0 <= py < H):
                continue
            if d < R_H:
                grid[py][px] = "\033[48;5;16m \033[0m"  # pure black bg
            elif d < R_H + 1:
                # Photon ring — bright thin ring
                grid[py][px] = "\033[38;5;229m●\033[0m"

    # Draw
    sys.stdout.write("\033[H")
    for row in grid:
        sys.stdout.write("".join(row))
        sys.stdout.write("\n")
    sys.stdout.flush()

    time.sleep(0.035)
