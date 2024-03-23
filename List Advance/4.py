nums = input().split(', ')
nums_pos = [int(num) for num in nums]
nums_neg = [int(num) for num in nums]
nums_even = [int(num) for num in nums]
nums_odd = [int(num) for num in nums]
positive = [number for number in nums_pos if int(number) >= 0]
negative = [number for number in nums_neg if int(number) < 0]
even = [number for number in nums_even if int(number) % 2 == 0]
odd = [number for number in nums_odd if int(number) % 2 != 0]
print("Positive:", ', '.join(map(str, positive)))
print("Negative:", ', '.join(map(str, negative)))
print("Even:", ', '.join(map(str, even)))
print("Odd:", ', '.join(map(str, odd)))
