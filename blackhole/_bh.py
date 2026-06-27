#!/usr/bin/env python3
"""Black hole animation engine for stderr consumption.

Usage: _bh.py <command> [args...]

Runs the command, streams stderr into a black hole animation in real-time,
and prints buffered stdout after the command exits.
"""
import os
import sys
import time
import math
import random
import signal
import shutil
import subprocess
import threading
import queue


# ── Constants ────────────────────────────────────────────────────────────────
FPS = 30
FRAME_DT = 1.0 / FPS
MIN_COLS = 60
MIN_ROWS = 20

# Black hole physics constants (tuned for terminal visualization)
G_M = 5000.0           # Gravitational parameter (G * M), tuned for terminal
R_S_FACTOR = 12        # Event horizon = min(col, row) / R_S_FACTOR
PHOTON_SPHERE_FACTOR = 1.5  # Photon sphere = 1.5 * r_s
ACCRETION_INNER_FACTOR = 2.0   # Accretion disk inner edge
ACCRETION_OUTER_FACTOR = 8.0   # Accretion disk outer edge
ACCRETION_PARTICLES = 120      # Number of disk particles
DISK_TILT = 0.25               # Disk tilt factor (edge-on view)
CHAR_ACCRETION = "•"           # Character for accretion particles


# ── ANSI Escape Sequences ────────────────────────────────────────────────────
ESC = "\033"
CLEAR = f"{ESC}[2J{ESC}[H"
HIDE_CURSOR = f"{ESC}[?25l"
SHOW_CURSOR = f"{ESC}[?25h"
RESET = f"{ESC}[0m"


class Terminal:
    """Terminal size detection and ANSI helpers."""

    def __init__(self):
        self.cols, self.rows = self._get_size()

    def _get_size(self):
        try:
            size = shutil.get_terminal_size()
            return size.columns, size.lines
        except Exception:
            return 80, 24

    def clear(self):
        return CLEAR

    def hide_cursor(self):
        return HIDE_CURSOR

    def show_cursor(self):
        return SHOW_CURSOR

    def reset(self):
        return RESET


class BlackHoleAnimation:
    """Main animation class."""

    def __init__(self, command):
        self.command = command
        self.terminal = Terminal()
        self.running = False
        self.stderr_queue = queue.Queue()
        self.stdout_buffer = []
        self.proc = None
        self.stderr_thread = None
        self.stdout_thread = None

        # Black hole geometry (computed after terminal size is known)
        self.center_x = self.terminal.cols // 2
        self.center_y = self.terminal.rows // 2
        self.r_horizon = max(2, self.terminal.cols // R_S_FACTOR)
        self.r_photon = self.r_horizon * PHOTON_SPHERE_FACTOR
        self.r_accretion_inner = self.r_horizon * ACCRETION_INNER_FACTOR
        self.r_accretion_outer = self.r_horizon * ACCRETION_OUTER_FACTOR

        # Particle systems
        self.disk_particles = []
        self.text_chars = []

        # Initialize accretion disk
        self._init_disk()

        # Frame buffer grid: grid[y][x] = (char, (r, g, b) or None)
        self.grid = [[(" ", None) for _ in range(self.terminal.cols)] for _ in range(self.terminal.rows)]

        # Text consumption state
        self.stderr_eof = False

        # Fade distance: characters start fading at this distance from horizon
        self.fade_start_dist = self.r_accretion_outer * 0.6

    def run(self):
        """Main entry point."""
        # Check terminal size
        if self.terminal.cols < MIN_COLS or self.terminal.rows < MIN_ROWS:
            self._run_silent()
            return

        # Set up signal handlers
        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGWINCH, self._handle_resize)

        # Start subprocess
        self.proc = subprocess.Popen(
            self.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Start threads
        self.stderr_thread = threading.Thread(
            target=self._read_stderr,
            daemon=True,
        )
        self.stderr_thread.start()

        self.stdout_thread = threading.Thread(
            target=self._read_stdout,
            daemon=True,
        )
        self.stdout_thread.start()

        # Run animation
        self.running = True
        self._animate()

        # Clean up
        self._cleanup()

    def _read_stderr(self):
        """Read stderr from subprocess and put in queue."""
        for line in self.proc.stderr:
            self.stderr_queue.put(line)
        self.stderr_queue.put(None)  # Sentinel to signal end

    def _read_stdout(self):
        """Read stdout from subprocess and buffer it."""
        for chunk in iter(lambda: self.proc.stdout.read(4096), b""):
            try:
                self.stdout_buffer.append(chunk.decode("utf-8", errors="replace"))
            except Exception:
                pass

    def _animate(self):
        """Main animation loop."""
        # Clear screen, hide cursor
        sys.stdout.write(CLEAR + HIDE_CURSOR)
        sys.stdout.flush()

        last_time = time.monotonic()
        frame = 0

        while self.running:
            now = time.monotonic()
            dt = now - last_time
            last_time = now
            dt = min(dt, 0.1)  # Cap delta time

            # Drain stderr queue, spawn characters
            self._feed_stderr()

            # Update physics
            self._update(dt)

            # Render
            self._render(frame)

            frame += 1

            # Stop if command has exited AND stderr has been fully read
            cmd_done = self.proc.poll() is not None
            if cmd_done and self.stderr_eof:
                break

            # Safety: if command is done but stderr reader is stuck, stop anyway
            if cmd_done and frame > FPS * 15:  # 15 second max
                break

            # Sleep for frame time
            time.sleep(FRAME_DT - (time.monotonic() - now))

    def _init_disk(self):
        """Initialize accretion disk particles with Keplerian orbits."""
        for i in range(ACCRETION_PARTICLES):
            # Distribute particles logarithmically (more concentrated near center)
            t = i / ACCRETION_PARTICLES
            radius = self.r_accretion_inner + (self.r_accretion_outer - self.r_accretion_inner) * (
                (1 - t) ** 0.5
            )
            angle = random.uniform(0, 2 * math.pi)
            # Keplerian angular velocity: ω = sqrt(GM/r³)
            angular_velocity = math.sqrt(G_M / (radius ** 3))
            self.disk_particles.append(
                {
                    "radius": radius,
                    "angle": angle,
                    "angular_velocity": angular_velocity,
                }
            )

    def _feed_stderr(self):
        """Drain stderr queue and spawn characters."""
        while not self.stderr_queue.empty():
            data = self.stderr_queue.get()
            if data is None:
                self.stderr_eof = True
                break
            # Binary detection: skip if data contains null bytes
            if b"\x00" in data:
                continue
            # Convert bytes to string, spawn characters
            try:
                text = data.decode("utf-8", errors="replace")
            except Exception:
                text = str(data)
            for char in text:
                self._spawn_character(char)

    def _spawn_character(self, char):
        """Spawn a text character at a random screen edge with initial velocity."""
        # Pick random edge
        edge = random.choice(["top", "bottom", "left", "right"])
        if edge == "top":
            x = random.uniform(0, self.terminal.cols)
            y = -1.0
        elif edge == "bottom":
            x = random.uniform(0, self.terminal.cols)
            y = self.terminal.rows + 1.0
        elif edge == "left":
            x = -1.0
            y = random.uniform(0, self.terminal.rows)
        else:
            x = self.terminal.cols + 1.0
            y = random.uniform(0, self.terminal.rows)

        # Vector from character to center
        dx = self.center_x - x
        dy = self.center_y - y
        dist = math.sqrt(dx * dx + dy * dy) + 0.1

        # Unit vectors
        radial_x = dx / dist
        radial_y = dy / dist
        tangential_x = -radial_y  # Perpendicular, counterclockwise
        tangential_y = radial_x

        # Initial velocity: mostly radial (falling in) + some tangential (spin)
        # Speed based on distance: farther = slower start, gravity accelerates
        base_speed = 2.0 + random.uniform(0, 2.0)
        radial_factor = 0.6 + random.uniform(0, 0.3)  # 60-90% radial
        tangential_factor = 0.3 + random.uniform(0, 0.4)  # 30-70% tangential

        vx = (radial_x * radial_factor + tangential_x * tangential_factor) * base_speed
        vy = (radial_y * radial_factor + tangential_y * tangential_factor) * base_speed

        self.text_chars.append(
            {
                "char": char,
                "x": x,
                "y": y,
                "vx": vx,
                "vy": vy,
                "alive": True,
            }
        )

    def _handle_signal(self, signum, frame):
        """Handle SIGINT/SIGTERM: stop animation, restore terminal."""
        self.running = False

    def _handle_resize(self, signum, frame):
        """Handle terminal resize: update dimensions, scale particle positions."""
        old_cols, old_rows = self.terminal.cols, self.terminal.rows
        self.terminal = Terminal()
        new_cols, new_rows = self.terminal.cols, self.terminal.rows

        # Recalculate black hole geometry
        self.center_x = new_cols // 2
        self.center_y = new_rows // 2
        self.r_horizon = max(2, new_cols // R_S_FACTOR)
        self.r_photon = self.r_horizon * PHOTON_SPHERE_FACTOR
        self.r_accretion_inner = self.r_horizon * ACCRETION_INNER_FACTOR
        self.r_accretion_outer = self.r_horizon * ACCRETION_OUTER_FACTOR
        self.fade_start_dist = self.r_accretion_outer * 0.6

        # Scale text character positions proportionally
        if old_cols > 0 and old_rows > 0:
            sx = new_cols / old_cols
            sy = new_rows / old_rows
            for tc in self.text_chars:
                tc["x"] *= sx
                tc["y"] *= sy

        # Rebuild grid
        self.grid = [[(" ", None) for _ in range(new_cols)] for _ in range(new_rows)]

    def _update_disk(self, dt):
        """Update accretion disk particle orbits with relativistic corrections."""
        r_s = self.r_horizon
        for p in self.disk_particles:
            r = p["radius"]
            # Time dilation: proper time slows near horizon
            # dt_proper = dt * sqrt(1 - r_s/r)
            if r > r_s:
                dilation = math.sqrt(1 - r_s / r)
            else:
                dilation = 0.01  # Inside horizon, extremely slowed
            p["angle"] += p["angular_velocity"] * dt * dilation

    def _update_text_chars(self, dt):
        """Update text character physics: gravity, lensing, time dilation."""
        r_s = self.r_horizon
        r_photon = int(self.r_photon)

        for tc in self.text_chars:
            if not tc["alive"]:
                continue

            dx = self.center_x - tc["x"]
            dy = self.center_y - tc["y"]
            dist = math.sqrt(dx * dx + dy * dy)

            # Check if consumed by event horizon
            if dist < r_s:
                tc["alive"] = False
                continue

            # Check if escaped off screen
            if (
                tc["x"] < -50
                or tc["x"] > self.terminal.cols + 50
                or tc["y"] < -50
                or tc["y"] > self.terminal.rows + 50
            ):
                tc["alive"] = False
                continue

            # Gravitational acceleration: a = G*M / r²
            # Using a stronger G_M for text chars so they fall in noticeably
            G_M_text = G_M * 3.0
            accel = G_M_text / (dist * dist)
            accel_x = accel * dx / dist
            accel_y = accel * dy / dist

            # Time dilation: slows near horizon
            # dt_proper = dt * sqrt(1 - r_s/r)
            if dist > r_s:
                dilation = math.sqrt(1 - r_s / dist)
            else:
                dilation = 0.01

            # Gravitational lensing: tangential deflection near photon sphere
            # As character passes near r_photon, it gets deflected
            lensing_strength = 0.0
            if r_photon * 0.7 < dist < r_photon * 2.5:
                # Strongest near photon sphere
                lensing_strength = 1.0 / (1.0 + abs(dist - r_photon) * 0.5)

            # Apply acceleration (with time dilation)
            tc["vx"] += (accel_x + lensing_strength * accel * 0.3) * dt * dilation
            tc["vy"] += (accel_y + lensing_strength * accel * 0.3) * dt * dilation

            # Update position
            tc["x"] += tc["vx"] * dt
            tc["y"] += tc["vy"] * dt

            # Update fade/darken factors based on proximity to horizon
            # fade_factor: 1.0 far away, 0.0 at horizon
            if dist > self.fade_start_dist:
                tc["fade"] = 1.0
            elif dist < r_s:
                tc["fade"] = 0.0
            else:
                tc["fade"] = (dist - r_s) / (self.fade_start_dist - r_s)
            tc["fade"] = max(0.0, min(1.0, tc["fade"]))

    def _update(self, dt):
        """Update physics for all particles."""
        self._update_disk(dt)
        self._update_text_chars(dt)

    def _render_disk(self):
        """Render accretion disk particles onto the grid."""
        cx, cy = self.center_x, self.center_y
        tilt = DISK_TILT
        r_s = self.r_horizon

        for p in self.disk_particles:
            # 3D position in disk plane, tilted for edge-on view
            cos_a = math.cos(p["angle"])
            sin_a = math.sin(p["angle"])

            # Screen position (projected ellipse)
            x = cx + p["radius"] * cos_a
            y = cy + p["radius"] * sin_a * tilt

            ix, iy = int(x), int(y)
            if not (0 <= ix < self.terminal.cols and 0 <= iy < self.terminal.rows):
                continue

            # Gravitational redshift: inner particles hotter (brighter/whiter)
            # Color gradient: white/yellow (inner) → orange → red (outer)
            t_norm = (p["radius"] - r_s * ACCRETION_INNER_FACTOR) / (
                self.r_accretion_outer - r_s * ACCRETION_INNER_FACTOR
            )
            t_norm = max(0.0, min(1.0, t_norm))

            # Blackbody-inspired color: hot inner, cool outer
            r_c = int(255 * (1.0 - t_norm * 0.4))
            g_c = int(255 * max(0.0, 1.0 - t_norm * 1.8))
            b_c = int(255 * max(0.0, 1.0 - t_norm * 2.5))

            # Doppler boost: approaching side brighter, receding side dimmer
            # Approaching = sin(a) < 0 (top half moving toward viewer in our tilt)
            doppler = 1.0 + sin_a * 0.4
            doppler = max(0.3, min(1.5, doppler))

            # Combine: gravitational redshift dims outer, Doppler modulates
            brightness = (1.0 - t_norm * 0.5) * doppler
            brightness = max(0.2, min(1.5, brightness))

            final_r = min(255, int(r_c * brightness))
            final_g = min(255, int(g_c * brightness))
            final_b = min(255, int(b_c * brightness))

            # Character brightness: brighter particles get more visible chars
            if brightness > 1.0:
                char = "*"
            elif brightness > 0.7:
                char = "●"
            elif brightness > 0.4:
                char = "•"
            else:
                char = "."

            # Grid collision: don't overwrite brighter pixels (prefer accretion over text)
            # For now, just set (text chars will handle priority in Task 3)
            self.grid[iy][ix] = (char, (final_r, final_g, final_b))

    def _render_text_chars(self):
        """Render text characters with fade/darken based on proximity to horizon."""
        for tc in self.text_chars:
            if not tc["alive"]:
                continue
            ix, iy = int(tc["x"]), int(tc["y"])
            if not (0 <= ix < self.terminal.cols and 0 <= iy < self.terminal.rows):
                continue

            # Base color: bright white/blue-white
            base_r, base_g, base_b = 230, 235, 245

            # Fade factor: 1.0 far away (full brightness), 0.0 at horizon (invisible)
            fade = tc.get("fade", 1.0)

            # Darken + fade: multiply color by fade factor
            # As fade -> 0, color approaches black (the void)
            final_r = int(base_r * fade)
            final_g = int(base_g * fade)
            final_b = int(base_b * fade)

            # Shadow effect: as characters get very close, add a dark/red tint
            # (simulating gravitational redshift / being pulled into darkness)
            if fade < 0.3:
                # Very close to horizon: dark red/brown shadow
                shadow_r = int(80 * (1.0 - fade) / 0.3)
                shadow_g = int(20 * (1.0 - fade) / 0.3)
                shadow_b = int(10 * (1.0 - fade) / 0.3)
                final_r = min(255, final_r + shadow_r)
                final_g = max(0, final_g - shadow_g)
                final_b = max(0, final_b - shadow_b)

            # Character size progression: use smaller/dimmer chars as fade decreases
            if fade > 0.7:
                char = tc["char"]
            elif fade > 0.4:
                char = "." if tc["char"].isalnum() else tc["char"]
            else:
                char = "."

            self.grid[iy][ix] = (char, (final_r, final_g, final_b))

    def _render_event_horizon(self):
        """Render event horizon as a black circle (void)."""
        cx, cy = self.center_x, self.center_y
        r = self.r_horizon

        # Clear cells inside the event horizon (make them background)
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if dx * dx + dy * dy <= r * r:
                    x, y = cx + dx, cy + dy
                    if 0 <= x < self.terminal.cols and 0 <= y < self.terminal.rows:
                        # Set to background (black/void)
                        self.grid[y][x] = (" ", (0, 0, 0))

    def _render_photon_sphere(self):
        """Render photon sphere as a bright ring at 1.5× r_s."""
        cx, cy = self.center_x, self.center_y
        r = int(self.r_photon)
        thickness = max(1, int(r * 0.15))  # Ring thickness

        for dy in range(-r - thickness, r + thickness + 1):
            for dx in range(-r - thickness, r + thickness + 1):
                dist = math.sqrt(dx * dx + dy * dy)
                if r - thickness / 2 <= dist <= r + thickness / 2:
                    x, y = cx + dx, cy + dy
                    if 0 <= x < self.terminal.cols and 0 <= y < self.terminal.rows:
                        # Bright white/yellow glow
                        self.grid[y][x] = ("○", (255, 255, 230))

    def _render(self, frame):
        """Render the frame: event horizon + photon sphere + accretion disk + text chars."""
        # Clear grid
        for y in range(self.terminal.rows):
            for x in range(self.terminal.cols):
                self.grid[y][x] = (" ", None)

        # Draw layers back-to-front
        self._render_event_horizon()
        self._render_photon_sphere()
        self._render_disk()
        self._render_text_chars()

        # Build ANSI output string
        out = CLEAR + self.terminal.hide_cursor()
        for y in range(self.terminal.rows):
            for x in range(self.terminal.cols):
                char, color = self.grid[y][x]
                if char == " " and color is None:
                    continue
                if color is not None:
                    out += f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
                out += f"\033[{y + 1};{x + 1}H{char}"
        out += RESET + f"\033[{self.terminal.rows + 1};1H"

        sys.stdout.write(out)
        sys.stdout.flush()

    def _cleanup(self):
        """Clean up after animation: restore terminal, print stdout."""
        # Show cursor and reset
        try:
            sys.stdout.write(SHOW_CURSOR + RESET)
            sys.stdout.flush()
        except Exception:
            pass

        # Print buffered stdout
        if self.stdout_buffer:
            try:
                sys.stdout.write("".join(self.stdout_buffer))
                sys.stdout.flush()
            except Exception:
                pass

        # Kill subprocess if still running
        if self.proc and self.proc.poll() is None:
            try:
                self.proc.terminate()
                self.proc.wait(timeout=1)
            except Exception:
                try:
                    self.proc.kill()
                except Exception:
                    pass

    def _run_silent(self):
        """Run command without animation (terminal too small or no stderr)."""
        self.proc = subprocess.run(self.command)
        sys.exit(self.proc.returncode)


def main():
    if len(sys.argv) < 2:
        print("Usage: _bh.py <command> [args...]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1:]
    anim = BlackHoleAnimation(command)
    anim.run()


if __name__ == "__main__":
    main()
