input_list = input()
beggars = int(input())
list_1 = input_list.split(', ')
list_2 = []
for i in range(beggars):
    list_2.append(0)
for i in range(len(list_1)):
    list_2[i % beggars] += int(list_1[i])
print(list_2)