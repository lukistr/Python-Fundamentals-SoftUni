cards = input().split(' ')
shuffles = int(input())
for _ in range(shuffles):
    n = len(cards)
    mid = n // 2
    shuffled_cards = []
    for i in range(mid):
        shuffled_cards.append(cards[i])
        shuffled_cards.append(cards[i + mid])
    cards = shuffled_cards
print(cards)