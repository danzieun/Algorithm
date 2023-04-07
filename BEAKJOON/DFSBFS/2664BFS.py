# 촌수계산 BFS

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def bfs(v, cnt):
    global result
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result[i] = result[v] + 1

bfs(a, 0)

if result[b] != 0:
    print(result[b])
else:
    print(-1)