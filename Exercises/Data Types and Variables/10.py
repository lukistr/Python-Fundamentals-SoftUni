import math
lost = int(input())
helm = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
helm = math.floor(lost / 2) * helm
sword = math.floor(lost / 3) * sword
shield = math.floor(lost / 6) * shield
armor = math.floor(lost / 12) * armor

expenses = helm + sword + shield + armor
print(f'Gladiator expenses: {expenses:.2f} aureus')
