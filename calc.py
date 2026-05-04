"""Simple calculator module — with a few bugs for the sandbox to find."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b  # BUG: no zero division handling


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # BUG: empty list crashes


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return low  # BUG: should return high
    return value
