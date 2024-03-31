capacity = int(input())

users = {}

while True:
    command = input()
    if command == "Statistics":
        break

    parts = command.split("=")
    action = parts[0]

    if action == "Add":
        username = parts[1]
        sent = int(parts[2])
        received = int(parts[3])
        if username not in users:
            users[username] = sent + received
        else:
            users[username] += sent + received

    elif action == "Message":
        sender = parts[1]
        receiver = parts[2]
        if sender in users and receiver in users:
            users[sender] += 1
            users[receiver] += 1
            if users[sender] >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]
            if users[receiver] >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif action == "Empty":
        username = parts[1]
        if username == "All":
            users.clear()
        elif username in users:
            del users[username]

print(f"Users count: {len(users)}")
for username, messages in users.items():
    print(f"{username} - {messages}")
