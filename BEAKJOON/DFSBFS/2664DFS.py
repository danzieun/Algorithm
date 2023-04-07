# 촌수계산 DFS

import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def dfs(v, cnt):
    global result
    cnt += 1
    visited[v] = True

    if v == b:
        result = cnt

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)

dfs(a, 0)
print(result-1)