def is_perfect_number(number):
    divisor_sum = sum(i for i in range(1, int(number / 2) + 1) if number % i == 0)

    if divisor_sum == number:
        return True
    else:
        return False

num = int(input())
if is_perfect_number(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
