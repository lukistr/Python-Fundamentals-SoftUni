username = input()

while True:
    command = input()
    if command == "Registration":
        break

    tokens = command.split()
    action = tokens[0]

    if action == "Letters":
        case = tokens[1]
        if case == "Lower":
            username = username.lower()
        elif case == "Upper":
            username = username.upper()
        print(username)
    elif action == "Reverse":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            reversed_substring =  username[start_index:end_index + 1][::-1]
            print(reversed_substring)
    elif action == "Substring":
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif action == "Replace":
        char = tokens[1]
        username = username.replace(char, "-")
        print(username)
    elif action == "IsValid":
        char = tokens[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
