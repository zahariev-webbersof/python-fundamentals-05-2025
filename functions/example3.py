def calculate_result(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'add': num1 + num2,
        'subtract': num1 - num2,
    }.get(operator)


operator_ = input()
num1_ = int(input())
num2_ = int(input())
result = calculate_result(operator_, num1_, num2_)
print(result)