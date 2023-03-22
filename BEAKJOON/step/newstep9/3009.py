list = [list(map(int, input().split())) for _ in range(3)]

x = 0
y = 0
if list[0][0] == list[1][0]:
    if list[1][0] != list[2][0]:
        x = list[2][0]
elif list[0][0] != list[1][0]:
    if list[1][0] == list[2][0]:
        x = list[0][0]
    elif list[0][0] == list[2][0]:
        x = list[1][0]

if list[0][1] == list[1][1]:
    if list[1][1] != list[2][1]:
        y = list[2][1]
elif list[0][1] != list[1][1]:
    if list[1][1] == list[2][1]:
        y = list[0][1]
    elif list[0][1] == list[2][1]:
        y = list[1][1]

print(x, y)
