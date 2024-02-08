import sys
input = sys.stdin.readline

N,M = map(int, input().split())
comb = []

def combination(num):
    if len(comb) == M:
        print(' '.join(map(str, comb)))
        return

    for i in range(num,N+1):
        comb.append(i)
        combination(i)
        comb.pop()

combination(1)