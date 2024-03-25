def add_and_subtract():
    a = int(input())
    b = int(input())
    c = int(input())

    def sum_numbers(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    sums = sum_numbers(a, b)
    return subtract(sums, c)

print(add_and_subtract())