import sys
input = sys.stdin.readline

N,M = map(int, input().split())
num_lst = list(map(int,input().split()))
num_lst.sort()
comb = []
def combination(num):
    if len(comb) == M:
        print(' '.join(map(str, comb)))
        return

    for i in range(num,N):
        if num_lst[i] not in comb:
            comb.append(num_lst[i])
            combination(i+1)
            comb.pop()

combination(0)