decoration = int(input())
days = int(input())
spirit_lost = int(days / 10)
spirit = 0
prize = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        decoration += 2
    if i % 2 == 0:
        prize += (2 * decoration)
        spirit += 5
    if i % 3 == 0:
        prize += (8 * decoration)
        spirit += 13
    if i % 5 == 0:
        prize += (15 * decoration)
        spirit += 17
    if i % 5 == 0 and i % 3 == 0:
        spirit += 30
    if i % 10 == 0:
        spirit -= 20
        prize += 23
    if i == days and i % 10 == 0:
        spirit -= 30
print(f'Total cost: {prize}')
print(f'Total spirit: {spirit}')