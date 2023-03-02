count = int(input())
divisor = list(map(int, input().split()))

if count == 1:
    result = divisor[0] * divisor[0]
else:
    result = min(divisor) * max(divisor)

print(result)