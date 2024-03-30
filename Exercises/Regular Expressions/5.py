def calculate_total_cost(purchases):
    total_cost = sum(price * quantity for price, quantity in purchases.values())
    return total_cost

purchased_furniture = {}

while True:
    input_str = input()
    if input_str == "Purchase":
        break

    parts = input_str.split("<<")
    furniture_name = parts[1].split(">>")[0]
    price_str, quantity_str = parts[1].split("!")

    try:
        price = float(price_str)
        quantity = int(quantity_str)
    except ValueError:
        continue

    if furniture_name in purchased_furniture:
        purchased_furniture[furniture_name][1] += quantity
    else:
        purchased_furniture[furniture_name] = [price, quantity]

total_cost = calculate_total_cost(purchased_furniture)

print("Bought furniture:")
for furniture_name, (price, quantity) in purchased_furniture.items():
    print(f"{furniture_name}")
print(f"Total money spend: {total_cost:.2f}")
