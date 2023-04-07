# 바이러스 BFS

import sys
from collections import deque

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

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        result.append(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return len(result) - 1

print(bfs(1))