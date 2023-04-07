# 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

t = int(input())

def dfs(a, b):
    if a < 0 or a >= m or b < 0 or b >= n:
        return False
    
    if graph[b][a] == 1:
        graph[b][a] = 0

        dfs(a-1, b)
        dfs(a+1, b)
        dfs(a, b-1)
        dfs(a, b+1)

        return True
    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1

    print(result)