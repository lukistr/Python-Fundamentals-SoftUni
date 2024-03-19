string1 = input()
string2 = input()
last = string1
for i in range(len(string1)):
    left = string2[:i + 1]
    right = string1[i + 1:]
    result = left + right
    if result != last:
        print(result)
        last = result
