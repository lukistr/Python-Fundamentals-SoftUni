n = int(input())

for i in range(1,n+1):
    string = input()
    check = True
    for j in range(len(string)):
        if string[j] == ',' or string[j] == '.' or string[j] == '_':
            check = False
    if check:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
