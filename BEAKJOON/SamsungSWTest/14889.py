# 스타트와 링크

import sys
input = sys.stdin.readline
from itertools import combinations, permutations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
n_list = [i for i in range(n)]  # 사람 번호
start_t = list(combinations(n_list, int(n/2)))   # n/2명 선택 (스타트 팀)
link_t = list(reversed(start_t))

start_score = 0
link_score = 0
result = []
for i in range(len(start_t)):
    start_p = list(permutations(start_t[i], 2))
    link_p = list(permutations(link_t[i], 2))

    for j in range(len(start_p)):
        start_score += s[start_p[j][0]][start_p[j][1]]
        link_score += s[link_p[j][0]][link_p[j][1]]
   
    result.append(abs(start_score - link_score))
    start_score = 0
    link_score = 0

print(min(result))