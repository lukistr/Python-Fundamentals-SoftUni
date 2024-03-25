n = int(input())
sums = 0
for i in range(n):
    litre = int(input())
    if sums + litre < 256:
        sums += litre
    else:
        print('Insufficient capacity!')
print(sums)
