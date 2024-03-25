def sum_of_digits(num):
    odd_num = 0
    even_num = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            even_num += int(digit)
        else:
            odd_num += int(digit)
    return f'Odd sum = {odd_num}, Even sum = {even_num}'

input_number = int(input())
print(sum_of_digits(input_number))