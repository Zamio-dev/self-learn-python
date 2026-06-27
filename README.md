# Docker + Python — My Learning Journey

I'm teaching myself Python using Docker as the environment, and this repo is a running diary of that effort.

**Why Docker?** I want a clean, isolated space to write Python without worrying about clashing with my system Python version, missing libraries, or accidentally breaking something. Docker gives me a fresh instance every time, lets me shut it down clean, and is a skill I'll use professionally anyway.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Docker Setup](#docker-setup)
3. [What I'm Learning](#what-im-learning)
   1. [Strings](#1-strings)
   2. [Numbers](#2-numbers)
   3. [Types and Type Casting](#3-types-and-type-casting)
   4. [Loops](#4-loops)
   5. [Functions](#5-functions)
   6. [Missing Basics](#6-missing-basics)
   7. [Terminal Art](#7-terminal-art)
4. [Data Files](#data-files)
5. [Where I'm Going](#where-im-going)

---

## Getting Started

This runs the Python environment I've defined:

```bash
docker compose up
```

That's it — it spins up a container using my `Dockerfile` and runs the scripts I've been working through.

## Docker Setup<a id="docker-setup"></a>

### Dockerfile

```dockerfile
FROM python:3.14-alpine3.24
WORKDIR /app
CMD ["python","myapp.py"]
```

Pretty lean — Python 3.14 on Alpine Linux (a minimal distro), working directory at `/app`. The container runs `myapp.py` by default.

### Docker Compose

```yaml
services:
  app:
    container_name: my-pyapp
    build:
      context: .
    volumes:
      - data:/app/python
      - .:/app

volumes:
  data:
```

Names the container `my-pyapp`, builds from the Dockerfile, and maps the local directory into the container so I can edit and see changes instantly without rebuilding. Also sets up a persistent data volume.

---

## What I'm Learning<a id="what-im-learning"></a>


### 1. Strings (`strings.py` / `strings.py`)

From basic slicing to formatting — the full string toolkit, explained.

**Quick start** — `strings.py`:

```python
message = """
hi how are you
i think things will get better
"""
```

- `message[:10]` → first 10 characters
- `message[5:]` → everything from character 5 onward
- `message[-5:]` → last 5 characters
- `message.upper()` / `.lower()` / `.title()` → case changes
- `message.strip()` → remove extra whitespace
- `message.find('will')` → index of a substring (or `-1` if not found)
- `message.replace('will','may')` → swap words, returns a new string
- `'you' in message` → existence check, returns `True`/`False`

`strings.py` goes much further:

- `capitalize()` vs `swapcase()` vs `title()` — when to use which
- `lstrip()` / `rstrip()` — especially useful when reading files (that trailing `\n`)
- `startswith()` / `endswith()` — great for file extension checks
- `split()` / `join()` — breaking sentences into words, gluing lists back together (the CSV workflow)
- `isdigit()` / `isalpha()` / `isalnum()` — input validation
- `zfill()` — pad numbers with zeros (`"7"` → `"0007"`, like room numbers)
- `center()` / `ljust()` / `rjust()` — align text for tables
- Escape characters: `\n`, `\t`, `\"`, `\\`
- `len()` — length checks (password validation, word counts)
- F-string formatting: `{price:.2f}`, `{salary:,.2f}` for money
- `.format()` method and old-school `%` formatting

---

### 2. Numbers (`integer.py`)

Arithmetic, rounding, formatting, and the weird operators Python throws at you.

**Quick start** — `integer.py`:

```python
10/3      # 3.333...  (true division)
10//3     # 3         (floor division)
10%3      # 1         (remainder)
10**3     # 1000      (exponentiation)
10^3      # 9         (bitwise XOR — not power!)
```

Learning note: `^` in Python is **not** exponentiation — that's `**`. `^` is bitwise XOR. A trap for anyone coming from other languages.


- `!s` / `!r` in f-strings — debug output
- `round()`, `math.ceil()`, `math.floor()` — when to use each
- `hex()`, `oct()`, `bin()` — number bases (colors, file permissions, binary)
- Format specifiers: `{42:05d}` for zero-padding, `{salary:,.2f}` for commas
- `divmod()` — get quotient and remainder in one step
- `pow(base, exp, mod)` — modular exponentiation (cryptography)
- Python handles arbitrarily large integers — no overflow
- Comparison chaining: `18 <= age < 65` — write math naturally
- `math.gcd()` / `math.lcm()` — great common divisor, least common multiple
- Multiple assignment and swapping: `a, b = b, a`

---

### 3. Types and Type Casting (`data_type_typecasting.py`)

Python's built-in types and how to convert between them.

**Quick start** — `data_type_typecasting.py`:

```python
variable_1 = 1                  # int
variable_2 = "this is a string" # str
variable_3 = 1.32               # float
variable_5 = True               # bool
variable_7 = [1, 2, 3, 4]       # list
variable_8 = {"name": "Sameer"} # dict
variable_9 = {1, 2, 3, 4}       # set
variable_10 = b"hello"          # bytes
```


- Full coverage of `None` ("nothing here" — like an empty parking spot)
- Tuple as immutable data (like temple coordinates — fixed, permanent)
- `set()` for removing duplicates ("no place visited twice")
- Detailed casting walkthroughs: `int ↔ float`, `str ↔ int`, `list ↔ tuple`, `list → set` (dedup)

---

### 4. Loops (`loops.py`)

Repetition, iteration, and the Pythonic ways to do it.

- `for` loop — go through a list (shopping list scenario)
- `enumerate()` — get item index while looping
- `range()` — count down, count up, countdown before liftoff
- Accumulating totals in a loop (splitting the dinner bill)
- `zip()` — match two lists side by side (names to bills)
- `while` + `break` — keep asking until the user says "done"
- `for...else` — "completed without interruption" semantics (parking spot checker)
- Nested `for` + `if/else` (mini calendar with events)
- **List comprehension** — `[name.upper() for name in names]`
- **List comprehension with filter** — `[n for n in numbers if n % 2 == 0]`
- **Dict comprehension** — `{word: len(word) for word in words}`

---

### 5. Functions (`functions.py`)

From basic `def` to decorators — functions are where Python really shines.

This file uses `dataset.json` (a dataset of names and places) for real examples.

- Basic function with parameters
- `return` — giving back a result
- Default parameters (`discount(price, rate=0.1)`)
- `*args` — accept any number of positional arguments
- `**kwargs` — accept any number of keyword arguments
- `lambda` — one-line anonymous functions
- `map()` — apply a function to every item
- `filter()` — keep items matching a condition
- Nested functions and **closures** — inner function remembering outer variables
- Docstrings — documenting what a function does
- **Recursion** — factorial as a self-calling function
- **Decorators** — `@logger` wraps a function with extra behavior
- Passing functions as arguments (`apply_twice(double, 5)`)
- `global` vs `local` scope

---

### 6. Missing Basics (`basics_missing.py`)

The stuff you need but textbooks skip — this is the most practical file in the repo.

- **Lists** — `append()`, `insert()`, `remove()`, `pop()`, `sort()` vs `sorted()`
- **Tuples** — unpacking, packing, `count()`
- **Dictionaries** — `.get()` for safe access, `.update()`, `.keys()` / `.values()` / `.items()`, `.pop()` with default
- **Sets** — union (`|`), intersection (`&`), difference (`-`), `add()`, `discard()`
- **File handling** — `open()` with `with`, read/write/append modes, line-by-line reading
- **Error handling** — `try/except/else/finally`, custom exceptions
- **Classes & OOP** — `__init__`, methods, inheritance, `super().__init__()`
- **Modules & imports** — `import`, `from...import`
- **JSON** — `json.load()`, `json.dump()`, `json.dumps()` (read/write files and strings)
- **Regex** — `re.findall()`, `re.sub()`, pattern matching for phones and emails
- **datetime** — `now()`, `strftime()`, `timedelta`, `strptime()`
- **random** — `randint()`, `uniform()`, `choice()`, `shuffle()`, `sample()`
- **Generators** — `yield` for lazy, memory-efficient iteration
- **Context managers** — `with` statement internals, building your own
- **collections** — `Counter`, `defaultdict`

---

### 7. Terminal Art (`blackhole.py`)

A physics-based black hole animation that runs in the terminal. 280 particles spiral toward an event horizon with relativistic gravity, frame-dragging, and Doppler-shifted colors. All stdlib — no dependencies.

Also includes a companion tool in `blackhole/` — a zsh wrapper (`bh`) that pipes command error output into the black hole for a dramatic error visualization.

---

## Data Files

- **`dataset.json`** — A structured dataset of names (by religion/gender) and places (by city). Used by `functions.py` for `map`/`filter` examples and by `basics_missing.py` for JSON handling demos.

---

## Where I'm Going<a id="where-im-going"></a>

This is still a work in progress. Take each topic, start simple, then go deep with local context. More topics coming as I learn them.

The goal is simple: build understanding, one script at a time.
