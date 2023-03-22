import sys
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

rank = [1] * N
for i in range(N-1):
    for j in range(i+1, N):
        if a[i][0] > a[j][0]:
            if a[i][1] > a[j][1]:
                rank[j] += 1
        elif a[i][0] < a[j][0]:
            if a[i][1] < a[j][1]:
                rank[i] += 1

print(*rank)