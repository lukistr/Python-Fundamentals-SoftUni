def join_force_side(force_side, force_user, force_users):
    for side, users in force_users.items():
        if force_user in users:
            users.remove(force_user)
    if force_side not in force_users:
        force_users[force_side] = set()
    force_users[force_side].add(force_user)


def print_force_users(force_users):
    for force_side, users in sorted(force_users.items(), key=lambda x: (-len(x[1]), x[0])):
        if users:
            print(f"Side: {force_side}, Members: {len(users)}")
            for user in sorted(users):
                print(f"! {user}")

force_users = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        join_force_side(force_side, force_user, force_users)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        join_force_side(force_side, force_user, force_users)
        print(f"{force_user} joins the {force_side} side!")

print_force_users(force_users)
