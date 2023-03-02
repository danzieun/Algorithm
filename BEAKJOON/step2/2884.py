H, M = map(int, input().split())

time = H * 60 + M - 45
time_h = time // 60
time_m = time % 60

if time_h < 0:
    time_h = 24 + time_h
    print(time_h, time_m)
else:
    print(time_h, time_m)