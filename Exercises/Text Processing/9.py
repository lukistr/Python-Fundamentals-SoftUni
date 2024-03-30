def count_unique_symbols(message):
    unique_symbols = set(message.upper())
    return len(unique_symbols)


def rage_quit(input_string):
    rage_message = ""
    i = 0
    while i < len(input_string):
        char = input_string[i]
        if char.isalpha():
            string = input_string[i]
            i += 1
            while i < len(input_string) and input_string[i].isdigit():
                string += input_string[i]
                i += 1
            string, num = string[:-1], int(string[-1])
            rage_message += string.upper() * num
        else:
            i += 1

    unique_symbols_count = count_unique_symbols(rage_message)
    return unique_symbols_count, rage_message


# Input
input_string = input()

# Process input and get rage message
unique_symbols_count, rage_message = rage_quit(input_string)

# Output
print(f"Unique symbols used: {unique_symbols_count}")
print(rage_message)
