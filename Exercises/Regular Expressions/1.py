import re

def extract_numbers(string):
    numbers = re.findall(r'\d+', string)
    return numbers

input_strings = []
while True:
    string = input()
    if string:
        input_strings.append(string)
    else:
        break

all_numbers = []
for string in input_strings:
    numbers = extract_numbers(string)
    all_numbers.extend(numbers)

print(' '.join(all_numbers))
