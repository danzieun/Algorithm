A, B = map(int, input().split())
C = int(input())

time = A * 60 + B + C
time_h = time // 60
time_m = time % 60

if time_h >= 24:
    print(time_h - 24, time_m)
else:
    print(time_h, time_m)