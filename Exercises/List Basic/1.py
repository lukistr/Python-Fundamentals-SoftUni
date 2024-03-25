string = input()
list1 = string.split(' ')
for i in range(len(list1)):
    list1[i] = 0 - int(list1[i])
print(list1)
