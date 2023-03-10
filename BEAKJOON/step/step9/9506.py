a = []

while True:
    n = int(input())

    # 약수 배열 a에 넣기
    for i in range(1, n):
        if n % i == 0:
            a.append(i)

    # 만약 약수의 합과 n이 같으면
    if n == sum(a):
        # n = 출력
        print(n, '=', end=' ')
        for j in range(len(a)):               
            # 만약 a[0]이면 a[0] 출력
            if j == 0:
                print(a[j], end=' ')
            # 아니면 + a[1] + a[2] + ...
            else:
                print('+', a[j], end=' ')
        print()
    # -1이 입력되면 종료
    elif n == -1:
        break
    # 약수의 합과 n이 다르면 n is NOT perfect. 출력
    else:
        print(n, 'is NOT perfect.')
    a = [] 
