N = int(input())
list = [list(map(int, input().split())) for _ in range(N)]

x_list = []
y_list = []
for i in range(N):
    x_list.append(list[i][0])
    y_list.append(list[i][1])

max_x = max(x_list)
min_x = min(x_list)
max_y = max(y_list)
min_y = min(y_list)

print((max_x-min_x)*(max_y-min_y))