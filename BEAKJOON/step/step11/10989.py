import sys
input = sys.stdin.readline

N = int(input())
N_list = [0] * 10001

for _ in range(N):
    a = int(input())
    N_list[a] += 1

for i in range(10001):
    if N_list[i] != 0:
        for _ in range(N_list[i]):
            print(i)