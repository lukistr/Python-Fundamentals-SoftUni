password_validation = input()

while True:
    command_line = input().split()
    if command_line[0] == "Complete":
        break
    elif command_line[0] == "Make":
        if command_line[1] == "Upper":
            if command_line[2].isdigit():
                password_validation = password_validation[:int(command_line[2])] + password_validation[int(command_line[2])].upper() + password_validation[int(command_line[2]) + 1:]
                print(password_validation)
        elif command_line[1] == "Lower":
            if command_line[2].isdigit():
                password_validation = password_validation[:int(command_line[2])] + password_validation[int(command_line[2])].lower() + password_validation[int(command_line[2]) + 1:]
                print(password_validation)
    elif command_line[0] == "Insert":
        if 0 <= int(command_line[1]) <= len(password_validation):
            password_validation = password_validation[:int(command_line[1])] + command_line[2] + password_validation[int(command_line[1]):]
            print(password_validation)
    elif command_line[0] == "Replace":
        if command_line[1] in password_validation:
            replaced_char = chr(ord(command_line[1]) + int(command_line[2]))
            password_validation = password_validation.replace(command_line[1], replaced_char)
            print(password_validation)
    elif command_line[0] == "Validation":
        if len(password_validation) < 8:
            print("Password must be at least 8 characters long!")
        if not password_validation.isalnum() and "_" not in password_validation:
            print("Password must consist only of letters, digits and _!")
        if not any(char.isupper() for char in password_validation):
            print("Password must consist at least one uppercase letter!")
        if not any(char.islower() for char in password_validation):
            print("Password must consist at least one lowercase letter!")
        if not any(char.isdigit() for char in password_validation):
            print("Password must consist at least one digit!")
