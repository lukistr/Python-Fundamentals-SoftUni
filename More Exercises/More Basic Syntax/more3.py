string = input()
array = string.split(', ')
num = 0
for i in range(0, len(array)):
    if array[i] == 'wolf':
        num = i
if num + 1 == len(array):
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {len(array) - 1 - num}! You are about to be eaten by a wolf!')
