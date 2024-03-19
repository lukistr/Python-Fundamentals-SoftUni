import math

biscuit = int(input())
workers = int(input())
otherFactory = int(input())
ownFactory = 0
perDay = biscuit * workers

for i in range(1, 31):
    if i % 3 == 0:
        ownFactory += math.floor(perDay * 0.75)
    else:
        ownFactory += perDay

print(f'You have produced {ownFactory} biscuits for the past month.')
percentage = 0
difProd = float(ownFactory) - float(otherFactory)
if ownFactory > otherFactory:
    percentage = (difProd / float(otherFactory)) * 100
    print(f'You produce {percentage:0.2f} percent more biscuits.')
else:
    percentage = ((difProd / otherFactory) * 100) * -1
    print(f'You produce {percentage:0.2f} percent less biscuits.')