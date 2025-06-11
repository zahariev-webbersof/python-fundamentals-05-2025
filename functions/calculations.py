def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return int(a / b)


def calculator():
    operation = input()
    num1 = int(input())
    num2 = int(input())
    result = 0

    if operation == 'add':
        result = add(num1, num2)

    elif operation == 'subtract':
        result = subtract(num1, num2)

    elif operation == 'multiply':
        result = multiply(num1, num2)

    elif operation == 'divide':
        result = divide(num1, num2)

    print(result)


calculator()
