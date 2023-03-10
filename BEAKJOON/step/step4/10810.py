import sys

N, M = map(int, sys.stdin.readline().split())

N_list = [0 for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    for i in range(a-1, b):
        N_list[i] = c

print(*N_list)