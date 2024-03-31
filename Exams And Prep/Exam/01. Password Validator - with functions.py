password = input()

def make_upper(index):
    global password
    password = password[:index] + password[index].upper() + password[index+1:]
    print(password)

def make_lower(index):
    global password
    password = password[:index] + password[index].lower() + password[index+1:]
    print(password)

def insert_char(index, char):
    global password
    if 0 <= index <= len(password):
        password = password[:index] + char + password[index:]
        print(password)

def replace_char(char, value):
    global password
    if char in password:
        ascii_value = ord(char)
        new_ascii_value = ascii_value + value
        new_char = chr(new_ascii_value)
        password = password.replace(char, new_char)
        print(password)

def validate_password():
    global password
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    if not password.isalnum() and "_" not in password:
        print("Password must consist only of letters, digits and _!")
    if not any(char.isupper() for char in password):
        print("Password must consist at least one uppercase letter!")
    if not any(char.islower() for char in password):
        print("Password must consist at least one lowercase letter!")
    if not any(char.isdigit() for char in password):
        print("Password must consist at least one digit!")

while True:
    command = input().split()
    if command[0] == "Complete":
        break
    action = command[0]
    if action == "Make":
        index = int(command[2])
        if command[1] == "Upper":
            make_upper(index)
        elif command[1] == "Lower":
            make_lower(index)
    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        insert_char(index, char)
    elif action == "Replace":
        char = command[1]
        value = int(command[2])
        replace_char(char, value)
    elif action == "Validation":
        validate_password()
