"""Simple calculator module — with a few bugs for the sandbox to find."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def average(numbers):
    if not numbers:
        raise ValueError("cannot average empty list")
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return low  # BUG: should return high
    return value
