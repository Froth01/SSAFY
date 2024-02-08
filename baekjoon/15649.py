import sys
input = sys.stdin.readline

N,M = map(int, input().split())
comb = []

def combination():
    if len(comb) == M:
        print(' '.join(map(str, comb)))
        return

    for i in range(1,N+1):
        if i not in comb:
            comb.append(i)
            combination()
            comb.pop()

combination()