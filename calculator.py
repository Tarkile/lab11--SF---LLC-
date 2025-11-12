"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD

=======
>>>>>>> 330cce7b73dc5d035f8fb370dd908e941eb34f99
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
<<<<<<< HEAD
        raise ZeroDivisionError("division by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("logarithm inputs must be positive")
    return math.log(b, a)
=======
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm inputs must be positive and base cannot be 1")
    return math.log(a, b)
>>>>>>> 330cce7b73dc5d035f8fb370dd908e941eb34f99

def exp(a, b):
    return a ** b





