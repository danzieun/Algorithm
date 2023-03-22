import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
N_list = list(map(int, input().split()))

sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            a = N_list[i] + N_list[j] + N_list[k]
            if a > M:
                pass
            else:
                sum = max(sum, a)

print(sum)