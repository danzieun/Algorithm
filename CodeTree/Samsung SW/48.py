# 싸움땅

n, m, k = map(int, input().split())
gun = [list(map(int, input().split())) for _ in range(n)]
player = [list(map(int, input().split())) for _ in range(m)]

print(player)

for i in range(m):
    gun[player[i][0]-1][player[i][1]-1] = 'p' + str(i+1)

while k != 0:
    if player[0][2] == 2:
        player[0][1] += 1

    k -= 1

print(gun)