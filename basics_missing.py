# All the basics you need but haven't learned yet 
# One file, all topics, simple examples

import os
import re
import random
import json
from datetime import datetime, timedelta
from collections import Counter

print("====>  Missing Basics <====\n")

# ========== 1. LISTS — operations you should know ==========
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")           # add to end
fruits.insert(1, "orange")       # add at position
print(f"After insert: {fruits}")  # ['apple', 'orange', 'banana', 'cherry', 'mango']

fruits.remove("banana")          # remove by value
last = fruits.pop()              # remove & return last
print(f"After pop: {fruits}")    # ['apple', 'orange', 'cherry', 'mango']

nums = [3, 1, 4, 1, 5, 9]
nums.sort()                      # sort in place
print(f"Sorted: {nums}")         # [1, 1, 3, 4, 5, 9]

reversed_nums = sorted(nums)     # return new sorted list
print(f"Reversed: {reversed_nums}")

# ========== 2. TUPLES — fixed lists ==========
# Like coordinates — you can't change where the temple is
coordinates = (9.2, 76.3)
print(f"\nCoordinates: {coordinates}")

# Unpack: extract values into variables
x, y = coordinates
print(f"x={x}, y={y}")

# Packing
point = 10, 20, 30
print(f"Packed: {point}")

# Tuple methods
count = (1, 2, 2, 3, 2).count(2)  # how many 2s?
print(f"Count of 2: {count}")       # 3

# ========== 3. DICTIONARIES — methods you need ==========
student = {"name": "Appu", "age": 25, "grade": "A"}

# Add new key
student["city"] = "Mavelikara"

# Safe access (no error if key missing)
phone = student.get("phone", "N/A")
print(f"\nStudent: {student}")
print(f"Phone (safe): {phone}")  # "N/A"

# Update multiple at once
student.update({"phone": "9876543210", "course": "Python"})

# Get all keys, values, items
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Pop with default
result = student.pop("height", "not found")
print(f"Pop height: {result}")  # "not found"

# ========== 4. SETS — unique items, math operations ==========
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date"}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union — all items from both
print(f"Union: {set_a | set_b}")  # {'apple', 'banana', 'cherry', 'date'}

# Intersection — items in both
print(f"Intersection: {set_a & set_b}")  # {'banana', 'cherry'}

# Difference — in A but not B
print(f"A - B: {set_a - set_b}")  # {'apple'}

# Add/remove
set_a.add("elderberry")
set_a.remove("apple")  # error if not exists
set_a.discard("apple")  # no error

# ========== 5. FILE HANDLING — read, write, append ==========
# Write (creates new or overwrites)
with open("test.txt", "w") as f:
    f.write("Hello from Kerala\n")
    f.write("Appu is learning Python\n")

# Read all at once
with open("test.txt", "r") as f:
    content = f.read()
print(f"\nFile content:\n{content}")

# Read line by line
print("Line by line:")
with open("test.txt", "r") as f:
    for line in f:
        print(f"  > {line.strip()}")

# Append (add to end, don't overwrite)
with open("test.txt", "a") as f:
    f.write("New line added\n")

print(f"File size: {os.path.getsize('test.txt')} bytes")

# ========== 6. ERROR HANDLING — don't crash ==========
# Basic try/except — demo with known values (not input, so it runs without a terminal)
try:
    value = int("abc")  # will raise ValueError
except ValueError:
    print("  Caught: that's not a number!")

try:
    result = 100 / 0
except ZeroDivisionError:
    print("  Caught: can't divide by zero!")
except Exception as e:
    print(f"  Caught: {e}")
else:
    print("  No errors — success!")
finally:
    print("  This always runs (cleanup code)")

# Custom exception
class InsufficientBalanceError(Exception):
    pass

balance = 100
def withdraw(amount):
    if amount > balance:
        raise InsufficientBalanceError(f"Only ₹{balance} available")
    return balance - amount

try:
    withdraw(200)
except InsufficientBalanceError as e:
    print(f"Error: {e}")

# ========== 7. CLASSES & OOP — organize your code ==========
class Houseboat:
    def __init__(self, name, capacity, route):
        self.name = name
        self.capacity = capacity
        self.route = route
    
    def info(self):
        return f"{self.name}: {self.capacity} people, {self.route}"
    
    def __str__(self):
        return self.info()

boat = Houseboat("Swathi", 12, "Alleppey to Kollam")
print(f"\n{boat}")  # "Swathi: 12 people, Alleppey to Kollam"

# Inheritance — houseboat can be luxury
class LuxuryBoat(Houseboat):
    def __init__(self, name, capacity, route, has_pool):
        super().__init__(name, capacity, route)
        self.has_pool = has_pool
    
    def luxury_info(self):
        return f"{self.info()} | Pool: {'Yes' if self.has_pool else 'No'}"

lux = LuxuryBoat("Royal", 20, "Backwaters", True)
print(lux.luxury_info())

# ========== 8. MODULES & IMPORTS — use code from other files ==========
import math
print(f"\nMath: sqrt(16) = {math.sqrt(16)}")

from datetime import datetime
now = datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Create utils.py with:
# def add(a, b): return a + b
#
# Then in another file:
# from utils import add
# print(add(5, 10))  # 15

# ========== 9. JSON — you have dataset.json, learn to use it ==========
# Read JSON
with open("dataset.json") as f:
    data = json.load(f)

# Note: names are grouped by religion in the dataset
all_males = [n for r in data['names'].values() for n in r['male']]
print(f"\nFirst male name (all religions): {all_males[0]}")

# Write JSON
info = {"name": "Lakshmi", "city": "Thrissur", "age": 30}
with open("output.json", "w") as f:
    json.dump(info, f, indent=2)

print(f"Written to output.json: {info}")

# JSON string (not file)
text = json.dumps({"key": "value"}, indent=2)
print(f"JSON string:\n{text}")

# ========== 10. USER INPUT — handle bad input ==========
# These examples show the pattern. Run interactively to test:
# name = input("Your name: ")
# print(f"Hello {name}!")
#
# while True:
#     age_str = input("Age (0-150): ")
#     if age_str.isdigit():
#         age = int(age_str)
#         if 0 < age < 150:
#             break
#     print("Invalid age, try again")
# print(f"Valid age: {age}")
print("User input: run this file interactively (python3 basics_missing.py) to test input")

# ========== 11. REGEX — pattern matching ==========
import re

text = "Call me at 9876543210 or email appu@gmail.com"

# Find all 10-digit numbers
phones = re.findall(r'\d{10}', text)
print(f"\nPhones: {phones}")  # ['9876543210']

# Find all emails
emails = re.findall(r'[\w.]+@[\w.]+', text)
print(f"Emails: {emails}")   # ['appu@gmail.com']

# Replace pattern
new_text = re.sub(r'\d{10}', 'XXXXXX', text)
print(f"Masked: {new_text}")  # "Call me at XXXXXX or email appu@gmail.com"

# ========== 12. DATETIME — dates and times ==========
now = datetime.now()
print(f"\nNow: {now}")
print(f"Formatted: {now.strftime('%d-%m-%Y %H:%M')}")

# Add days
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

# Subtract hours
three_hours_ago = now - timedelta(hours=3)
print(f"3 hours ago: {three_hours_ago.strftime('%H:%M')}")

# Parse string to datetime
date_str = "15-01-2024"
parsed = datetime.strptime(date_str, "%d-%m-%Y")
print(f"Parsed: {parsed}")

# ========== 13. RANDOM — random numbers and choices ==========
print(f"\nRandom int (1-100): {random.randint(1, 100)}")
print(f"Random float (0-1): {random.uniform(0, 1):.4f}")

# Choose from list
options = ["apple", "banana", "cherry", "mango"]
print(f"Random choice: {random.choice(options)}")

# Shuffle
names = ["Appu", "Lakshmi", "Niran", "Sibu"]
random.shuffle(names)
print(f"Shuffled: {names}")

# Sample without replacement
sample = random.sample(range(1, 50), 6)  # 6 numbers from 1-50
print(f"Lottery numbers: {sample}")

# ========== 14. GENERATORS — lazy iteration ==========
# yield instead of return — gives one value at a time
def counter(start, stop):
    n = start
    while n <= stop:
        yield n
        n += 1

print(f"\nGenerator example:")
for i in counter(1, 5):
    print(f"  {i}", end=" ")
print()

# Memory efficient for large data
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# ========== 15. CONTEXT MANAGERS — with statement deep dive ==========
# You use with for files, but also for locks, transactions, timing

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        print(f"  Time: {self.elapsed:.4f}s")

print(f"\nTimer example:")
with Timer():
    sum(range(100000))  # do something slow

# ========== BONUS: COLLECTIONS — useful utilities ==========
# Counter — count occurrences
fruits_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(fruits_list)
print(f"\nFruit counts: {counts}")  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common
print(f"Most common: {counts.most_common(1)}")  # [('apple', 3)]

# defaultdict — auto-create missing keys
from collections import defaultdict
groups = defaultdict(list)
for name in ["Appu", "Lakshmi", "Niran", "Appu"]:
    groups[name[0]].append(name)  # group by first letter
print(f"Groups: {dict(groups)}")  # {'A': ['Appu', 'Appu'], 'L': ['Lakshmi'], 'N': ['Niran']}

print("\n====>  Done!  <====")
