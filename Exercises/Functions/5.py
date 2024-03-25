def is_even(number):
    return number % 2 == 0

numbers_input = input()
numbers_list = list(map(int, numbers_input.split()))

print(list(filter(is_even, numbers_list)))
