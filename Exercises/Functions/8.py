def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def check_palindromes(numbers_list):
    numbers = [int(num) for num in numbers_list.split(', ')]
    palindromes = [is_palindrome(num) for num in numbers]

    return palindromes

numbers_input = input()
palindrome_results = check_palindromes(numbers_input)

for result in palindrome_results:
    print(result)
