def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    if a > b:
        return a - b
    else:
        return b - a
def division(a, b):
    if a == 0 or b == 0:
        print(" infinite ")
    elif a > b:
        return a/b
    else:
        return b/a



