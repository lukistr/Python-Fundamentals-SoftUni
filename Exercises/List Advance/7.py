numbers = input().split(', ')
numbers = [int(num) for num in numbers]
max_num = max(numbers)
group_max = ((max_num // 10) + 1) * 10
for i in range(10, group_max + 1, 10):
    group = [num for num in numbers if num <= i]
    numbers = [num for num in numbers if num not in group]
    if i == group_max and len(group) == 0:
        break
    else:
        print(f"Group of {i}'s: {group}")
