string = input()
coffee = 0
while not string == 'END':
    if string.lower() == 'coding' or string.lower() == 'cat' or string.lower() == 'dog' or string.lower() == 'movie':
        if string == string.lower():
            coffee += 1
        else:
            coffee += 2
    string = input()
if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)
