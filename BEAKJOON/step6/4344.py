import sys

C = int(sys.stdin.readline())

for _ in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    mean = sum(score[1:]) / score[0]
    high = [i for i in range(1, score[0]+1) if score[i] > mean]
    print('%.3f' %((len(high)/score[0])*100), '%', sep='')