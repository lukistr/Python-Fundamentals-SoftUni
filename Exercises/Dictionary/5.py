def obtain_legendary_item(inventory):
    legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
    for material, quantity in inventory.items():
        if material in legendary_items and quantity >= 250:
            print(f"{legendary_items[material].capitalize()} obtained!")
            quantity = quantity - 250
            return quantity
    return None

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

while True:
    line = input().lower().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1]
        if material in key_materials:
            key_materials[material] += quantity
            obtained_item = obtain_legendary_item(key_materials)
            if obtained_item:
                key_materials[material] = obtained_item
                break
        else:
            if material in junk_items:
                junk_items[material] += quantity
            else:
                junk_items[material] = quantity
    else:
        continue
    break

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in sorted(junk_items.items()):
    print(f"{material}: {quantity}")
