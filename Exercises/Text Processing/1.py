import re

def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9_-]{3,16}$', username) is not None

usernames = input().split(", ")

for username in usernames:
    if is_valid_username(username):
        print(username)
