import sys

W, N = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a.sort(key = lambda x: x[1], reverse=True)

price = 0
for i in range(N):
    if a[i][0] >= W:
        price += W * a[i][1]
        break
    else:
        price += a[i][0] * a[i][1]
        W = W - a[i][0]

print(price)