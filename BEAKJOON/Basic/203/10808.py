S = list(input())
S_list = [0] * 26

for i in S:
    S_list[ord(i)-97] += 1

print(*S_list)