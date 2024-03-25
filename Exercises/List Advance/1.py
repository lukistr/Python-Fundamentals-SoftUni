# first_list = input().split(', ')
# second_list = input().split(', ')
#
# new_list = {word for word in first_list for x in second_list if word in x}
# result = sorted(item for item in new_list)
# print(result)

input1 = input().split(', ')
input2 = input().split(', ')
output = [word for word in input1 if any(word in string for string in input2)]
print(output)