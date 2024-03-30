dictionary = {}
while True:
    text = input()
    if text == 'stop':
        break

    number = int(input())
    if text in dictionary:
        dictionary[text] += number
    else:
        dictionary[text] = number
for key, value in dictionary.items():
    print(f'{key} -> {value}')
