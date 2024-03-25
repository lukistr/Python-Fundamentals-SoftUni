import math
m = int(input())
n = int(input())
result = 0
for i in range(1, n + 1):
    result += 50
    if i % 15 == 0:
        m += 5
    if i % 10 == 0:
        m -= 2
    if i % 3 == 0 and i % 5 == 0:
        result -= (m * 2)
    if i % 3 == 0:
        result -= (m * 3)
    if i % 5 == 0:
        result += (20 * m)
    result -= (m * 2)
print(f'{m} companions received {math.floor(result / m)} coins each.')
