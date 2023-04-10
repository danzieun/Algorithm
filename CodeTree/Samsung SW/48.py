# 싸움땅

n, m, k = map(int, input().split())
gun = [list(map(int, input().split())) for _ in range(n)]
player = [list(map(int, input().split())) for _ in range(m)]
power = [0] * m
visited = [[0] * n for _ in range(n)]
result = [0] * m

def d(p):
    # visited 초기화
    visited[p[0] - 1][p[1] - 1] = 0
    if p[2] == 0:
        if p[1] - 1 >= 1 and p[1] - 1 <= 5:
            p[1] -= 1
        else:
            p[1] += 1
            p[2] = 2
    if p[2] == 1:
        if p[0] + 1 >= 1 and p[0] + 1 <= 5:
            p[0] += 1
        else:
            p[0] -= 1
            p[2] = 3
    if p[2] == 2:
        if p[1] + 1 >= 1 and p[1] + 1 <= 5:
            p[1] += 1
        else:
            p[1] -= 1
            p[2] = 0
    if p[2] == 3:
        if p[0] - 1 >= 1 and p[0] - 1 <= 5:
            p[0] -= 1
        else:
            p[1] += 1
            p[2] = 1

def d2(p):
    if p[2] == 0:
        if p[1] - 1 >= 1 and p[1] - 1 <= 5 and visited[p[0] - 2][p[1] - 2] == 0:
            p[1] -= 1
        else:
            if p[0] + 1 >= 1 and p[0] + 1 <= 5 and visited[p[0]][p[1]] == 0:
                p[0] += 1
                p[2] = 1
    if p[2] == 1:
        if p[0] - 1 >= 1 and p[0] - 1 <= 5:
            p[0] += 1
        else:
            p[0] -= 1
            p[2] = 3
    if p[2] == 2:
        if p[1] - 1 >= 1 and p[1] - 1 <= 5:
            p[1] += 1
        else:
            p[1] -= 1
            p[2] = 0
    if p[2] == 3:
        if p[0] - 1 >= 1 and p[0] - 1 <= 5:
            p[0] -= 1
        else:
            p[1] += 1
            p[2] = 1

for i in range(k):
    for j in range(m):
        p = player[j]
        d(p)   
        if gun[p[0]-1][p[1]-1] != 0:
            if visited[p[0]-1][p[1]-1] == 0:
                a = power[j]
                b = gun[p[0]-1][p[1]-1]
            
                power[j] = max(a, b)
                gun[p[0]-1][p[1]-1] = min(a, b)
                visited[p[0]-1][p[1]-1] = j
            else:
                if p[3] + power[j] > player[visited[p[0]-1][p[1]-1]] + power[visited[p[0]-1][p[1]-1]]:
                    result[j] = (p[3] + power[j]) - (player[visited[p[0]-1][p[1]-1]] + power[visited[p[0]-1][p[1]-1]])
                    gun[visited[p[0]-1][p[1]-1]] = power[visited[p[0]-1][p[1]-1]]
                    power[visited[p[0]-1][p[1]-1]] = 0
                    d(visited[p[0]-1][p[1]-1])
                elif p[3] + power[j] < player[visited[p[0]-1][p[1]-1]] + power[visited[p[0]-1][p[1]-1]]:
                    result[visited[p[0]-1][p[1]-1]] = (player[visited[p[0]-1][p[1]-1]] + power[visited[p[0]-1][p[1]-1]]) - (p[3] + power[j])
                    gun[p[0]-1][p[1]-1] = power[j]
                    power[j] = 0  
                    d(j)

print(power)
print(gun) 
print(player)
print(result)