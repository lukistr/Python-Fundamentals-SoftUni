import re

text = input()
sand = re.findall('sand', text.lower())
water = re.findall('water', text.lower())
sun = re.findall('sun', text.lower())
fish = re.findall('fish', text.lower())

print(len(sand) + len(water) + len(sun) + len(fish))
