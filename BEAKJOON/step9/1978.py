import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

a = []
cnt = 0
for i in N_list:
    if i != 1:
        for j in range(1, int(i ** 1/2)+1):
            if i % j == 0:
                a.append(j)

        if len(a) == 1:
            cnt = cnt + 1
        a = []

print(cnt)
