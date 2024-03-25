n = int(input())
w = 0
t = 0
q = 0
ball = 0
for i in range(n):
    w1 = int(input())
    t1 = int(input())
    q1 = int(input())
    sums = (w1 / t1) ** q1
    if sums > ball:
        ball = sums
        q = q1
        w = w1
        t = t1

print(f'{w} : {t} = {int(ball)} ({q})')
