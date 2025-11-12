# https://github.com/Tarkile/lab11--SF---LLC-
# partner 1: Samuel Finlinson
# partner 2: Leonardo Lopez-Casula

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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Logarithm inputs must be positive and base cannot be 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b





