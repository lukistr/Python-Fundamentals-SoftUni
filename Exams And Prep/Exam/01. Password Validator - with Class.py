class PasswordManager:
    def __init__(self, password):
        self.password = password

    def make_upper(self, index):
        if 0 <= index < len(self.password):
            self.password = self.password[:index] + self.password[index].upper() + self.password[index+1:]
            print(self.password)

    def make_lower(self, index):
        if 0 <= index < len(self.password):
            self.password = self.password[:index] + self.password[index].lower() + self.password[index+1:]
            print(self.password)

    def insert_char(self, index, char):
        if 0 <= index <= len(self.password):
            self.password = self.password[:index] + char + self.password[index:]
            print(self.password)

    def replace_char(self, char, value):
        if char in self.password:
            ascii_value = ord(char)
            new_ascii_value = ascii_value + value
            new_char = chr(new_ascii_value)
            self.password = self.password.replace(char, new_char)
            print(self.password)

    def validate_password(self):
        if len(self.password) < 8:
            print("Password must be at least 8 characters long!")
        if not self.password.isalnum() and "_" not in self.password:
            print("Password must consist only of letters, digits and _!")
        if not any(char.isupper() for char in self.password):
            print("Password must consist at least one uppercase letter!")
        if not any(char.islower() for char in self.password):
            print("Password must consist at least one lowercase letter!")
        if not any(char.isdigit() for char in self.password):
            print("Password must consist at least one digit!")

password = input()
manager = PasswordManager(password)

while True:
    command = input().split()
    if command[0] == "Complete":
        break
    action = command[0]
    if action == "Make":
        index = int(command[2])
        if command[1] == "Upper":
            manager.make_upper(index)
        elif command[1] == "Lower":
            manager.make_lower(index)
    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        manager.insert_char(index, char)
    elif action == "Replace":
        char = command[1]
        value = int(command[2])
        manager.replace_char(char, value)
    elif action == "Validation":
        manager.validate_password()
