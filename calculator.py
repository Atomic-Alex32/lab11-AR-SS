# https://github.com/Atomic-Alex32/lab11-AR-SS
# Partner 1: Alex Rivera
# Partner 2: Stefan Sisljagic

"""
calculator.py
- Defines functions used to create a simple calculator
"""

import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError 
    return b / a 

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    math.log(b, a)

def exponent(a, b):
    math.pow(a, b)

