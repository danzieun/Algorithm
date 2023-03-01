import sys

K, P, N = map(int, sys.stdin.readline().split())

count = K * pow(P, N, 1000000007)

print(count % 1000000007)