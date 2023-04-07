N, M = map(int, input().split())
ice_map = [list(map(int, input())) for _ in range(M)]

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if ice_map[x][y] == 0:
        ice_map[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)