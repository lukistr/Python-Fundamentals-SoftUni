budget = float(input())
flour = float(input())
eggs = flour * 0.75
milk = (flour * 1.25) / 4
price = flour + eggs + milk
result = int(budget / price)
colored_eggs = 0
for i in range(1, result + 1):
    colored_eggs += 3
    if i % 3 == 0:
        colored_eggs -= (i - 2)
print(f'You made {result} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget - (result * price):.2f}BGN left.')
