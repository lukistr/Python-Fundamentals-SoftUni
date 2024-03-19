orders = int(input())
total = 0
for i in range(orders):
    prize = float(input())
    days = int(input())
    needs = int(input())
    if 0.01 <= prize <= 100 and 1 <= days <= 31 and 1 <= needs <= 2000:
        price = prize * days * needs
        total += price
        print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total:.2f}')
