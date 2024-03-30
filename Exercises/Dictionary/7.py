def register_user(username, license_plate, database):
    if username in database:
        print(f"ERROR: already registered with plate number {database[username]}")
    else:
        database[username] = license_plate
        print(f"{username} registered {license_plate} successfully")

def unregister_user(username, database):
    if username not in database:
        print(f"ERROR: user {username} not found")
    else:
        del database[username]
        print(f"{username} unregistered successfully")

def print_registered_users(database):
    for username, license_plate in database.items():
        print(f"{username} => {license_plate}")

registered_users = {}

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_plate = command[2]
        register_user(username, license_plate, registered_users)
    elif command[0] == "unregister":
        username = command[1]
        unregister_user(username, registered_users)

print_registered_users(registered_users)
