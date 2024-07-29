def add(a, b):
    return a + b

def subtract(a, b):
    if b>a:
        a,b=b,a
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
