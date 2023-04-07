# 단지번호붙이기

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
count = 0
count_list = []

def dfs(x, y):  
    global count

    if x < 0 or x >= n or y < 0 or y >= n:
        return False
       
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            count_list.append(count)
            count = 0

count_list.sort()

print(result)
for i in range(result):
    print(count_list[i])