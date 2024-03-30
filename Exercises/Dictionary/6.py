products = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]['quantity'] += quantity
        if products[name]['price'] != price:
            products[name]['price'] = price
    else:
        products[name] = {'price': price, 'quantity': quantity}

for name, info in products.items():
    total_price = info['price'] * info['quantity']
    print(f"{name} -> {total_price:.2f}")
