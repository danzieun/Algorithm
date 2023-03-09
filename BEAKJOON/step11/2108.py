from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

N_list = [int(input()) for _ in range(N)]
N_list.sort()

cnt = Counter(N_list)
mode = cnt.most_common()

print(round(sum(N_list)/N))
print(N_list[N//2])
a = []
if len(mode) != 1:
    if mode[0][1] == mode[1][1]:
        for i in range(len(mode)):
            if mode[i][1] == mode[0][1]:
                a.append(mode[i][0])
        print(int(a[1]))
    else:
        print(int(mode[0][0]))
else:
    print(N_list[0])
print(N_list[N-1]-N_list[0])