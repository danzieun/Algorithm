# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

from collections import Counter

t = int(input())

for num in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    cnt = Counter(n_list)
    cnt = cnt.most_common()

    print('#%d' %n, cnt[0][0])