# https://github.com/Atomic-Alex32/lab11-AR-SS
# Partner 1: Alex Rivera
# Partner 2: Stefan Sisljagic

"""
calculator.py
- Defines functions used to create a simple calculator
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



def logarithm(a, b):
    if b <= 0:
        raise ValueError
    math.log(b, a)

def exponent(a, b):
    math.pow(a, b)

def add(a,b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def log(a,b):
    if b<= 0:
        raise ValueError
    return math.log(b,a)

def exp(a,b):
    return a ** b

