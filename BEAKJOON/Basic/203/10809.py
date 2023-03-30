S = input()
S_list = [-1] * 26

for i in range(len(S)):
    if S_list[ord(S[i])-97] == -1:
        S_list[ord(S[i])-97] = i

print(*S_list)