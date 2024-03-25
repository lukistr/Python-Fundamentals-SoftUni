fires = input().split("#")
water = int(input())

total_effort = 0
total_fire_put_out = 0
cells_put_out = []

for fire in fires:
    fire_type, fire_value = fire.split(" = ")
    fire_value = int(fire_value)

    if fire_type == "High":
        valid_range = range(81, 126)
    elif fire_type == "Medium":
        valid_range = range(51, 81)
    elif fire_type == "Low":
        valid_range = range(1, 51)
    else:
        continue

    if fire_value in valid_range and water >= fire_value:
        water -= fire_value
        total_fire_put_out += fire_value
        effort = (fire_value * 0.25)
        total_effort += effort
        cells_put_out.append(fire_value)

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")