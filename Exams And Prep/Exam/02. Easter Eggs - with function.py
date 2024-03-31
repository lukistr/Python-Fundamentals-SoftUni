import re

def find_valid_eggs(text):
    pattern = r'([@#]+)([a-z]{3,})([@#])[^\w\d]*?\/(\d+)\/'
    eggs = re.findall(pattern, text)
    for egg in eggs:
        color = egg[1]
        amount = egg[3]
        print(f"You found {amount} {color} eggs!")

text = input()
find_valid_eggs(text)
