num = input()
array = []
result = ''
for i in num:
    array.append(i)
array.sort(reverse=True)

for i in range(0,len(array)):
    result += array[i]
print(int(result))
