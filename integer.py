# Numbers and integer operations
# I am learning python
# Like Appu, Lakshmi, Aranmula, Thrissur Pooram etc.

import math

print("====>  Numbers and Integer Operations <====\n")

# ========== 1. BASIC ARITHMETIC ==========

appu_shops = 4      # Appu bought 4 mundus
lakshmi_shops = 3   # Lakshmi bought 3 mundus
total_shops = appu_shops + lakshmi_shops
print(f"Appu shops {appu_shops} + Lakshmi shops {lakshmi_shops} = {total_shops}")

# Division — how many bananas per person?
total_bananas = 10
persons = 3
# Normal division gives decimal
print(f"\n{total_bananas / persons =:.2f}")  # 3.33 — each person gets 3.33 bananas (impossible!)
print("This is regular division, gives fractional result")

# Floor division — how many full bananas each person gets?
print(f"{total_bananas // persons =}")  # 3 — full bananas only, no fractions
print("Floor division (//) gives only the whole number part")

# Modulo — what's left after sharing?
print(f"{total_bananas % persons =}")  # 1 — one banana left over
print("Modulo (%) gives the remainder. Like: after sharing 10 bananas among 3, 1 left")

# Multiplication
print(f"\n10 bananas x 3 friends = {10 * 3 =}")

# Exponent — power of 2
# Like compounding interest: 2^10 means 2 multiplied by itself 10 times
print(f"2^10 (2 to the power 10) = {2 ** 10 =}")
# Used in: houseboat capacity doubling each year, compound interest etc.

# XOR — bitwise operation
# ^ means XOR. Used in cryptography and error checking.
# For beginners: XOR is 1 if bits differ, 0 if same
print(f"10 ^ 3 (XOR) = {10 ^ 3 =}")

# ========== 2. FORMATTED OUTPUT ==========

# !s = str version (shows the normal string representation)
# !r = repr version (shows how Python stores it internally)
# Both are useful when debugging

print(f"\n--- Formatted output examples ---")
print(f"10*3 with !s: {10*3=!s}")  # '30' — how you'd normally see it
print(f"10*3 with !r: {10*3=!r}")  # 30 — how Python stores it internally

# !s is like "show me the face"
# !r is like "show me the DNA"

# ========== 3. ROUNDING NUMBERS ==========

# round() — rounds to nearest integer (default) or to N decimals
print(f"\n--- Rounding ---")
print(f"round(10.006) = {round(10.006) =}")   # 10
print(f"round(10.5) = {round(10.5) =}")        # 10 — Python rounds to even! (banker's rounding)
print(f"round(10.51) = {round(10.51) =}")      # 11

# Round to 2 decimal places (useful for money)
price = 1250.756
print(f"Cardamom price rounded to 2 decimals: {round(price, 2) =}")  # 1250.76

# ========== 4. CEIL and FLOOR ==========

# ceil() — always round UP (ceiling is above you)
# Like: if you need 3.1 rooms, you need 4 rooms. You can't have 0.1 room!
print(f"\n--- Ceil and Floor ---")
print(f"math.ceil(10.007) = {math.ceil(10.007) =}")  # 11 — always rounds up
print(f"math.ceil(10.1) = {math.ceil(10.1) =}")      # 11
print(f"math.ceil(10.0) = {math.ceil(10.0) =}")      # 10 — already whole

# floor() — always round DOWN (floor is below you)
# Like: if you have 10.9 kg rice, you have 10 full kg
print(f"math.floor(10.007) = {math.floor(10.007) =}")  # 10 — always rounds down
print(f"math.floor(10.9) = {math.floor(10.9) =}")      # 10

# Real life use:
# ceil → number of buses needed (can't have fraction of a bus)
# floor → number of full boxes you can pack

# ========== 5. ABSOLUTE VALUE ==========

# abs() — distance is always positive, even if you go backwards
# If Appu walks -5 meters (backwards), distance is still 5 meters
print(f"\n--- Absolute value ---")
print(f"abs(-10.006) = {abs(-10.006) =}")  # 10.006 — distance can't be negative!

# ========== 6. HEX, OCTAL, BINARY — NUMBER BASES ==========

# Hex (base 16) — used for colors, memory addresses, permissions
# Like a secret code that computers speak
print(f"\n--- Number bases ---")
print(f"hex(255) = {hex(255) =}")    # '0xff' — this is how red is #FF0000 in CSS
print(f"hex(250) = {hex(250) =}")    # '0xfa'
print(f"hex(42) = {hex(42) =}")      # '0x2a'

# Octal (base 8) — used in Linux file permissions
# Like a simplified code for read/write/execute
print(f"oct(8) = {oct(8) =}")        # '0o10'
print(f"oct(64) = {oct(64) =}")      # '0o100'

# Binary (base 2) — what computers actually think in
# Each digit is a light switch: 0=off, 1=on
print(f"bin(10) = {bin(10) =}")      # '0b1010' — 10 written in binary
print(f"bin(255) = {bin(255) =}")    # '0b11111111' — all 8 switches ON!

# ========== 7. FORMAT SPECIFIERS — PRINT NUMBERS BEAUTIFULLY ==========

print(f"\n--- Format specifiers ---")
# Zero padding — like a parking spot number, always 4 digits
print(f"Pad with zeros: {42:05d}")         # 00042 — like room number 0042
print(f"Pad with zeros: {7:05d}")          # 00007

# Right align — pad spaces on the left
print(f"Right align: {42:>10}")            # '        42' — right aligned in 10 spaces
print(f"Left align: {42:<10}")             # '42        ' — left aligned in 10 spaces
print(f"Center align: {42:^10}")           # '    42    ' — centered in 10 spaces

# Comma separator for thousands — like writing salary
print(f"Comma thousands: {1000000:,}")     # 1,000,000 — easy to read salary!
print(f"Appu's monthly salary: ₹{50000:,.2f}")  # ₹50,000.00

# ========== 8. DIVMOD — GET QUOTIENT AND REMAINDER TOGETHER ==========

# Like sharing bananas: how many each person gets AND how many left
print(f"\n--- divmod() ---")
bananas = 47
friends = 5
quotient, remainder = divmod(bananas, friends)
print(f"{bananas} bananas shared among {friends} friends:")
print(f"Each gets: {quotient}, Leftover: {remainder}")
# Output: Each gets: 9, Leftover: 2

# Real life: you pay ₹47 for 5 items. Each item costs ₹9, ₹2 left over.
# divmod does both calculations in ONE step.

# ========== 9. POW — POWER WITH OPTIONAL MODULAR ARITHMETIC ==========

# Basic power
print(f"\n--- pow() ---")
print(f"pow(2, 10) = {pow(2, 10) =}")    # 1024 — 2 raised to power 10

# Advanced: pow(base, exponent, modulo)
# Like: 2^10 mod 3 — what's the remainder when 1024 is divided by 3?
# Used in cryptography (RSA encryption) and scheduling algorithms
print(f"pow(2, 10, 3) = {pow(2, 10, 3) =}")  # 1 — 1024 mod 3 = 1
print(f"Used in: houseboat scheduling, cryptography, hash functions")

# ========== 10. LARGE INTEGERS — PYTHON HANDLES THEM FOR FREE ==========

# Other languages have limits. Python doesn't.
# Like Kerala's population — grows forever, Python handles it.
print(f"\n--- Large integers ---")
huge_number = 2 ** 1000
print(f"2^1000 has {len(str(huge_number))} digits!")
print("That's a number with 301 digits. Python handles it without overflow.")
print("Other languages would crash. Python just keeps going.")

# ========== 11. COMPARISON CHAINING — WRITE MATH NATURALLY ==========

# You can chain comparisons like real math notation
print(f"\n--- Comparison chaining ---")
age = 25
# Instead of: age >= 18 and age < 65
# You can write: 18 <= age < 65 — natural, like writing on paper!
if 18 <= age < 65:
    print(f"Appu (age {age}) is an adult but not retired")

# Check if temperature is in a comfortable range
temp = 30
if 20 <= temp <= 35:
    print(f"Temperature {temp}°C is pleasant in here")

# ========== 12. GCD and LCM — MATH FUNCTIONS ==========

import math

# GCD — Greatest Common Divisor
# Like finding the biggest piece that divides two things equally
print(f"\n--- GCD and LCM ---")
print(f"GCD of 12 and 8 = {math.gcd(12, 8) =}")  # 4 — biggest number that divides both
# Used in: simplifying fractions, dividing land equally among heirs

# LCM — Least Common Multiple
# Like finding when two events happen together again
print(f"LCM of 4 and 6 = {math.lcm(4, 6) =}")   # 12 — first number divisible by both
# Used in: scheduling temple festivals, finding when two bus routes coincide

# ========== 13. MULTIPLE ASSIGNMENT — ASSIGN MANY VARIABLES AT ONCE ==========

# You can assign several values in one line
print(f"\n--- Multiple assignment ---")
appu, lakshmi, niran = 25, 30, 28
print(f"Appu={appu}, Lakshmi={lakshmi}, Niran={niran}")
# All assigned in one line. Clean. No repetitive code.

# Swap two values (no temporary variable needed!)
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")
# Python swaps them magically. No extra variable needed.
# In other languages you'd need: temp = a; a = b; b = temp
