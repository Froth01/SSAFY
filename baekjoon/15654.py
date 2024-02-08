import sys
input = sys.stdin.readline

N,M = map(int, input().split())
num_lst = list(map(int,input().split()))
num_lst.sort()
comb = []
def combination():
    if len(comb) == M:
        print(' '.join(map(str, comb)))
        return

    for i in num_lst:
        if i not in comb:
            comb.append(i)
            combination()
            comb.pop()

combination()