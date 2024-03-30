def sum_of_multiplied_character_codes(str1, str2):
    total_sum = 0
    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        total_sum += ord(str1[i]) * ord(str2[i])

    remaining_chars = str1[min_length:] + str2[min_length:]
    for char in remaining_chars:
        total_sum += ord(char)

    return total_sum

str1, str2 = input().split()

result = sum_of_multiplied_character_codes(str1, str2)

print(result)
