# 단지번호붙이기 DFS

import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []
cnt = 0

# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    else:
        if graph[x][y] == 1 and visited[x][y] == False:
            visited[x][y] = True

            global cnt
            cnt += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                dfs(nx, ny)
            
            return True
    return False

for x in range(n):
    for y in range(n):
        if dfs(x, y) == True:
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))

for i in result:
    print(i)
