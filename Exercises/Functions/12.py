def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

def divide_factorials(num1, num2):
    fact1 = factorial(num1)
    fact2 = factorial(num2)

    division_result = fact1 / fact2

    formatted_result = "{:.2f}".format(division_result)

    return formatted_result

num1 = int(input())
num2 = int(input())

result = divide_factorials(num1, num2)
print(result)
