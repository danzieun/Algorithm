# 토마토

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(k)]
visited = [[[False] * n for _ in range(m)] for _ in range(k)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
da = [0, 0, 0, 0, 1, -1]
db = [0, 0, -1, 1, 0, 0]
dc = [-1, 1, 0, 0, 0, 0]

for i in range(k):
    for _ in range(m):
        graph[i].append(list(map(int, input().split())))

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    while queue:
        a, b, c = queue.popleft()
        visited[c][b][a] = True
      
        for i in range(6):
            na = a + da[i]
            nb = b + db[i]
            nc = c + dc[i]

            if na >= 0 and na < n and nb >= 0 and nb < m and nc >= 0 and nc < k and graph[nc][nb][na] == 0 and visited[nc][nb][na] == False:
                graph[nc][nb][na] = graph[c][b][a] + 1
                queue.append((na, nb, nc))
                visited[nc][nb][na] = True

for a in range(n):
    for b in range(m):
        for c in range(k):
            if graph[c][b][a] == 1 and visited[c][b][a] == False:
                bfs(a, b, c)

print(graph)
result = 0
for a in range(n):
    for b in range(m):
        for c in range(k):
            if graph[c][b][a] == 0:
                print(-1)
                exit()
            else:
                result = max(result, graph[c][b][a])
print(result-1)