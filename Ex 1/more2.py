string = input()
array = []

for i in range(len(string)):
    if string[i] == string[i].upper() and 'a' <= string[i].lower() <= 'z':
        array.append(i)
print(array)
