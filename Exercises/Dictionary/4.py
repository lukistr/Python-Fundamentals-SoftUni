phonebook = {}
entry = input().split('-')
while True:
    if entry[0].isdigit():
        entry = int(entry[0])
        break
    name, number = entry
    phonebook[name] = number
    entry = input().split('-')

for _ in range(entry):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
