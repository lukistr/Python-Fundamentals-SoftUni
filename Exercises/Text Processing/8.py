def calculate_string_value(string):
    total_value = 0
    for i in range(len(string)):
        char = string[i]
        if char.isnumeric():
            number = int(char)
            if i > 0 and string[i - 1].isalpha():
                position = ord(string[i - 1].lower()) - ord('a') + 1
                if string[i - 1].isupper():
                    number /= position
                else:
                    number *= position

            if i < len(string) - 1 and string[i + 1].isalpha():
                position = ord(string[i + 1].lower()) - ord('a') + 1
                if string[i + 1].isupper():
                    number -= position
                else:
                    number += position

            total_value += number
    return total_value

input_strings = input().split()

total_sum = sum(calculate_string_value(string) for string in input_strings)

print(f"{total_sum:.2f}")
