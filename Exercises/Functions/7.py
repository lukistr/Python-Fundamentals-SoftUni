numbers_input = input()
numbers_list = list(map(int, numbers_input.split()))
print("The minimum number is", min(numbers_list))
print("The maximum number is", max(numbers_list))
print("The sum number is:", sum(numbers_list))