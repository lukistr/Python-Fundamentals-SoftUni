def is_valid_password(password):
    ret = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        ret = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        ret = False

    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 2:
        print("Password must have at least 2 digits")
        ret = False

    if ret:
        return True
    else:
        return False

password = input()
if is_valid_password(password):
    print("Password is valid")
