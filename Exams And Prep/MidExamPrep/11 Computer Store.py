computerPrice = 0
tax = 0
totalPrice = 0
while True:
    price = input()
    if price == 'special':
        tax = computerPrice / 5
        totalPrice = (computerPrice + tax) - ((computerPrice + tax) / 10)
        break
    elif price == 'regular':
        tax = computerPrice / 5
        totalPrice = computerPrice + tax
        break
    if float(price) > 0:
        computerPrice += float(price)
    else:
        print('Invalid price!')
if totalPrice > 0:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {computerPrice:0.2f}$')
    print(f'Taxes: {tax:0.2f}$')
    print('-----------')
    print(f'Total price: {totalPrice:0.2f}$')
else:
    print('Invalid order!')