import json

# Load dataset
with open('dataset.json') as f:
    data = json.load(f)



# ========== 1. BASIC FUNCTION ==========
# Define: take input, do something
def greet(name):
    print(f"Hello {name}")

greet("Appu")
greet("Lakshmi")

# ========== 2. RETURN VALUE ==========
# Function gives back a result
def add(a, b):
    return a + b

print(add(10, 20))  # 30

# ========== 3. DEFAULT PARAMETER ==========
# If not given, use default value
def discount(price, rate=0.1):
    return price * (1 - rate)

print(discount(100))       # 90.0 (10% off)
print(discount(100, 0.2))  # 80.0 (20% off)

# ========== 4. *ARGS (VARIABLE POSITIONAL) ==========
# Accept any number of arguments
def sum_prices(*prices):
    return sum(prices)

print(sum_prices(10, 20, 30, 40))  # 100
print(sum_prices(5, 15, 25))       # 45

# ========== 5. **KWARGS (VARIABLE KEYWORD) ==========
# Accept any number of keyword arguments
def guest_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

guest_info(name="Niran", age=25, city="Mavelikara")

# ========== 6. LAMBDA ==========
# One-line anonymous function
square = lambda x: x ** 2
print(square(5))  # 25

# ========== 7. MAP ==========
# Apply function to every item in a list
names = data['names']['hindu']['male'][:5]
upper_names = list(map(lambda n: n.upper(), names))
print(upper_names)  # ['ARJUN', 'ADITHYAN', 'KRISHNA', 'HARI', 'VISSHNU']

# ========== 8. FILTER ==========
# Keep items that match a condition
temples = data['places']['kozhikode']
long_names = list(filter(lambda p: len(p) > 15, temples))
print(long_names)

# ========== 9. NESTED FUNCTION ==========
# Function inside function
def outer():
    def inner():
        return "inner called"
    return inner()

print(outer())

# ========== 10. CLOSURE ==========
# Inner function remembers outer variable
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_5 = make_adder(5)
print(add_5(10))  # 15

# ========== 11. DOCSTRING ==========
# Document what function does
def is_prime(n):
    """Check if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False

# ========== 12. RECURSION ==========
# Function calls itself
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120 (5*4*3*2*1)

# ========== 13. DECORATOR ==========
# Wrap function with extra behavior
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(3, 4)  # Calling multiply with (3, 4)\nResult: 12

# ========== 14. FUNCTION AS ARGUMENT ==========
# Pass function to another function
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

print(apply_twice(double, 5))  # 20 (5*2=10, 10*2=20)

# ========== 15. GLOBAL vs LOCAL ==========
x = 100  # global

def change_x():
    x = 200  # local - doesn't change global
    print(f"Inside: {x}")

change_x()  # Inside: 200
print(x)    # 100 (global unchanged)
