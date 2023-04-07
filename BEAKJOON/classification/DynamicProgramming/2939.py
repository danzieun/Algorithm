# 설탕 배달

n = int(input())
d = [5001] * (n + 5)

d[3] = 1
d[5] = 1

for i in range(6, n+1):
    d[i] = min(d[i-3], d[i-5]) + 1

if d[n] < 5001:
    print(d[n])
else:
    print(-1)