N = int(input())
a = [input().split() for _ in range(N)]

a = sorted(a, key = lambda x : int(x[0]))

for i in range(N):
    print(int(a[i][0]), a[i][1])