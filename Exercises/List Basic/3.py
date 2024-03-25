cards = input()
list_1 = cards.split(' ')
list_1 = list(dict.fromkeys(list_1))
players_a = 11
players_b = 11
if len(cards) > 0:
    for i in list_1:
        if i[0] == 'A':
            players_a -= 1
        elif i[0] == 'B':
            players_b -= 1
        if (players_a < 7) or (players_b < 7):
            break
print(f'Team A - {players_a}; Team B - {players_b}')
if (players_a < 7) or (players_b < 7):
    print('Game was terminated')