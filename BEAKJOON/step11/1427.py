N = input()

# string -> list
N_list = []
for i in range(len(N)):
    N_list.append(N[i])

# 내림차순 정렬
N_list.sort(reverse=True)

# print
for i in range(len(N)):
    print(N_list[i], end='')