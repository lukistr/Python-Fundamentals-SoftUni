stock = {}

def receive_food(quantity, food):
    quantity = int(quantity)
    if quantity <= 0:
        return
    if food not in stock:
        stock[food] = 0
    stock[food] += quantity

def sell_food(quantity, food, sell_quantity):
    quantity = int(quantity)
    if food not in stock:
        print(f"You do not have any {food}.")
        return sell_quantity
    if stock[food] < quantity:
        sold_quantity = stock[food]
        del stock[food]
        print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
    else:
        stock[food] -= quantity
        print(f"You sold {quantity} {food}.")
        sell_quantity += quantity
        return sell_quantity

def print_stock():
    for food, quantity in stock.items():
        if quantity > 0:
            print(f"{food}: {quantity}")

sell_quantity = 0
while True:
    command = input().split()
    if command[0] == "Complete":
        print_stock()
        break
    action, quantity, food = command
    if action == "Receive":
        receive_food(quantity, food)
    elif action == "Sell":
        sell_quantity = sell_food(quantity, food, sell_quantity)
print(f"All sold: {sell_quantity} goods")
