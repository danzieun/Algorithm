# 토마토

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(k)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
da = [0, 0, 0, 0, 1, -1]
db = [0, 0, -1, 1, 0, 0]
dc = [-1, 1, 0, 0, 0, 0]

for i in range(k):
    for _ in range(m):
        graph[i].append(list(map(int, input().split())))

def bfs(a, b, c, cnt):
    queue = deque()
    queue.append((a, b, c))

    while queue:
        a, b, c = queue.popleft()
      
        for i in range(6):
            na = a + da[i]
            nb = b + db[i]
            nc = c + dc[i]

            if na >= 0 and na < n and nb >= 0 and nb < m and nc >= 0 and nc < k and graph[nc][nb][na] == 0:
                graph[nc][nb][na] = graph[c][b][a] + 1
                queue.append((na, nb, nc))
                cnt += 1

for a in graph:
    for b in a:
        for c in b:
            bfs(a, b, c, 1)

print(graph)
