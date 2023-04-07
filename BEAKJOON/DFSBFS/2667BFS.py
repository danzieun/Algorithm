# 단지번호붙이기 BFS

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            else:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    
    return cnt

for x in range(n):
    for y in range(n):
        if visited[x][y] == False and graph[x][y] == 1:
            result.append(bfs(x, y))

result.sort()

print(len(result))

for i in result:
    print(i)