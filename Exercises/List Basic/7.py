gifts = input().split()
command = input()

while command != "No Money":
    command_parts = command.split()
    action = command_parts[0]

    if action == "OutOfStock":
        gift_to_remove = command_parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"

    elif action == "Required":
        gift_to_replace = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_replace

    elif action == "JustInCase":
        gifts[-1] = command_parts[1]

    command = input()

filtered_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(filtered_gifts))