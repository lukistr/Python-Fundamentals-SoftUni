list_integer = input().split(' ')
remove_number = int(input())
for i in range(len(list_integer)):
    list_integer[i] = int(list_integer[i])
for _ in range(remove_number):
    list_integer.remove(min(list_integer))
result = str(list_integer[0])
list_integer.remove(list_integer[0])
for i in range(len(list_integer)):
    result += ', ' + str(list_integer[i])
print(result)