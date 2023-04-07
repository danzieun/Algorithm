s = input()
s_list = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

cnt = 0
for i in s_list:
    a = int(ord(s[0]) - 96) + i[0]
    b = int(s[1]) + i[1]
    
    if a >= 1 and a <= 8 and b >= 1 and b <= 8:
        cnt += 1

print(cnt)