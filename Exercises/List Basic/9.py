items_prices = input().split("|")
budget = float(input())

max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

bought_items_prices = []
profit = 0

for item_price in items_prices:
    item, price = item_price.split("->")
    price = float(price)

    if price <= max_prices[item] and budget >= price:
        budget -= price
        bought_items_prices.append(price * 1.40)
        profit += price * 0.40

print(" ".join([f"{price:.2f}" for price in bought_items_prices]))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")