# DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

dfs_list = []
bfs_list = []

def dfs(graph, v, visited):
    visited[v] = True
    dfs_list.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] =  True

    while queue:
        v = queue.popleft()
        bfs_list.append(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

dfs(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)
print(*dfs_list)
print(*bfs_list)