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
        comb.append(num_lst[i])
        combination(i)
        comb.pop()

combination(0)