import re

text_regex = input()
pattern = r'([@#]+)([a-z]{3,})([@#])[^\w\d]*?\/(\d+)\/'
eggs_found = re.findall(pattern, text_regex)
for egg in eggs_found:
    print(f"You found {egg[3]} {egg[1]} eggs!")
