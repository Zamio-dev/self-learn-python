# Docker + Python — My Learning Journey

I'm teaching myself Python using Docker as the environment, and this repo is a running diary of that effort.

**Why Docker?** I want a clean, isolated space to write Python without worrying about clashing with my system Python version, missing libraries, or accidentally breaking something. Docker gives me a fresh instance every time, lets me shut it down clean, and is a skill I'll use professionally anyway.

---

## Table of Contents

1. [Getting Started (One Line)](#getting-started)
2. [Dockerfile](#dockerfile)
3. [Docker Compose](#docker-compose)
4. [What I'm Learning in Python](#what-im-learning-in-python)
   1. [Strings](#1-strings)
   2. [Numbers](#2-numbers)
   3. [Types and Type Casting](#3-types-and-type-casting)
5. [Where I'm Going](#where-im-going)

---

## Getting Started

This runs the Python environment I've defined:

```bash
docker compose up
```

That's it — it spins up a container using my `Dockerfile` and runs the scripts I've been working through.

---

## Dockerfile<a id="dockerfile"></a>

```dockerfile
FROM python:3.14-alpine3.24
WORKDIR /app
CMD ["python","myapp.py"]
```

This is pretty lean — I'm using Python 3.14 on Alpine Linux (a minimal distro) and setting my working directory to `/app`. The container will run `myapp.py` by default.

## Docker Compose<a id="docker-compose"></a>

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

The compose file names my container (`my-pyapp`), builds from the Dockerfile, and maps my local code directory into the container so I can edit and see changes without rebuilding. It also sets up a persistent volume for data.

---

## What I'm Learning in Python <a id="what-im-learning-in-python"></a>

This repo tracks 3 topics so far — I'm adding more as I go along.

### 1. Strings (`strings.py`)<a id="1-strings"></a>

getting around Python's string toolkit:

```python
message = """
hi how are you
i think things will get better
"""
```

- `message[:10]` → first 10 characters
- `message[5:]` → everything from character 5 to the end
- `message[-5:]` → last 5 characters
- `message[-1:-7]` → slices in reverse (toward the left)
- `message.upper()` / `message.lower()` → change case
- `message.title()` → title case
- `message.strip()` → remove leading/trailing whitespace
- `message.find('will')` → index of a substring, or `-1` if not found
- `message.replace('will','may')` → returns a new string with substitutions
- `'you' in message` / `'you' not in message` → checks existence, returns `True`/`False`

---

### 2. Numbers (`integer.py`)<a id="2-numbers"></a>

Getting comfortable with arithmetic and formatting:

```python
import math
x = 4
y = 3
z = x + y  # 7

10/3      # 3.333...  (true division)
10//3     # 3         (floor division — rounds down)
10%3      # 1         (remainder)
10**3     # 1000      (exponentiation)
10^3      # 9         (bitwise XOR — not power!)

round(10.006)          # 10
math.ceil(10.007)      # 11 (round up)
math.floor(10.007)     # 10 (round down)
abs(-5)                # 5

print(f"{10/3=:.2f}")  # formatted output: 3.33
```

Learning note: the `^` operator in Python is *not* exponentiation (that's `**`), it's bitwise XOR. A common trap.

---

### 3. Types and Type Casting (`data_type_typecasting.py`)<a id="3-types-and-type-casting"></a>

Exploring the built-in types and how to convert between them:

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

Type conversion in action:

```python
type(float(variable_1))   # int → float
type(int(variable_3))     # float → int
str(int(variable_3))      # float → int → str
```

I'm getting comfortable with Python's `type()` function to check what a variable is, and the core cast functions (`int()`, `float()`, `str()`, `bool()`) to change between them.

---

## Where I'm Going<a id="where-im-going"></a>

This is a work in progress — more Python topics coming as I learn them.

The goal is simple: build understanding, one script at a time.
