names = input().split(' ')
my_name = [name for name in names if len(name) % 2 == 0]
for name in my_name:
    print(name)
