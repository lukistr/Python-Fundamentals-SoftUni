def right_angled_triangle(rows):
    result = ''
    for i in range(rows):
        if i < rows - 1:
            result += '*' * (i + 1) + '\n'
        else:
            result += '*' * (i + 1)
    return result

def square(rows):
    result = '*' * rows + '\n'
    if rows > 1:
        for i in range(rows - 2):
            result += '*' + ' ' * (rows - 2) + '*' + '\n'
        result += '*' * rows
        return result

def diamond(rows):
    result = ''
    reverse_result = ''
    for i in range(1, rows + 1, 2):
        result += ' ' * int((rows - i) / 2) + '*' * i + '\n'
    if rows % 2 == 0:
        rows = rows - 1
    for i in range(rows - 2, 0, -2):
        if i > 1:
            reverse_result += ' ' * int((rows - i) / 2) + '*' * i + '\n'
        else:
            reverse_result += ' ' * int((rows - i) / 2) + '*' * i
    result += reverse_result
    return result

if __name__ == '__main__':
    while True:
        print('What you want to draw?\n1. Right-angled Triangle\n2. Square with Hollow Center\n3. Diamond\n4. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 4:
            break
        else:
            row = int(input("Enter the number of rows: "))
            if choice == 1:
                print(right_angled_triangle(row))
            elif choice == 2:
                print(square(row))
            elif choice == 3:
                print(diamond(row))
