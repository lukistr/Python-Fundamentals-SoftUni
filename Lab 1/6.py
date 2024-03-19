number = int(input())
prise = input()

while prise != 'End':
    sums = int(prise)
    number = int(number) - sums
    if number < 0:
        print('You went in overdraft!')
        break
    prise = input()
else:
    print('You bought everything needed.')
