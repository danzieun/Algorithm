import sys

time = [list(map(str, input().split())) for _ in range(5)]
all = []

for i in range(5):
    start_time = time[i][0].split(':')
    end_time = time[i][1].split(':')
    all.append((int(end_time[0])*60 + int(end_time[1])) - (int(start_time[0])*60 + int(start_time[1])))

print(sum(all))