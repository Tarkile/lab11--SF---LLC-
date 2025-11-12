"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/Tarkile/lab11--SF---LLC-
#partner 1: Samuel Finlinson
#partner 2: Leonardo Lopez-Casula

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Error calculating hypotenuse: {e}")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm inputs must be positive and base cannot be 1")
    return math.log(a, b)

def exp(a, b):
    return a ** b





