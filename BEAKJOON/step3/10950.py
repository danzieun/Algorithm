T = int(input())

a = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    print(a[i][0] + a[i][1])