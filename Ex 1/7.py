string = input()

while not string == 'End':
    result = ''
    for char in string:
        result += char * 2
    if not string == 'SoftUni':
        print(result)
    string = input()
