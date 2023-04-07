# DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

dfs_list = []
bfs_list = []

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
    
def dfs(graph, v, dfs_visited):
    dfs_visited[v] = True
    dfs_list.append(v)

    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(graph, i, dfs_visited)

def bfs(graph, v, bfs_visited):
    queue = deque([v])
    bfs_visited[v] = True

    while queue:
        v = queue.popleft()
        bfs_list.append(v)

        for i in graph[v]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

dfs(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)

print(*dfs_list)
print(*bfs_list)