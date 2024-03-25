initial_energy = 100
initial_coins = 100
events = input().split("|")

energy = initial_energy
coins = initial_coins

for event in events:
    event_type, value = event.split("-")
    value = int(value)

    if event_type == "rest":
        if energy + value <= initial_energy:
            energy += value
            print(f"You gained {value} energy.")
        else:
            gained_energy = initial_energy - energy
            energy = initial_energy
            print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        energy -= 30
        if energy >= 0:
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            break

if coins >= value:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")