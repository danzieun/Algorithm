import sys

num = int(input())

a = [list(map(int, input().split())) for _ in range(num)]

for i in range(num):
    b = a[i][0] + a[i][1]
    print("Case #", i+1, ": ", b, sep='')