# 바이러스 DFS

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    
    return len(result)

print(dfs(1) - 1)