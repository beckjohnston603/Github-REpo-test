# Simple Calculator
# Calculator - Updated from GitHub Web Interface
<<<<<<< HEAD
#mergeeeeeeeeeeeeee
=======
#merge one

>>>>>>> c4be0f58fa65bd4c849f8bf96665336940bba4c0
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Calculator loaded!")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b
