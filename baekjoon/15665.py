import sys
input = sys.stdin.readline

N,M = map(int, input().split())
num_lst = list(map(int,input().split()))
num_lst.sort()
comb = []
result = []
def combination():
    if len(comb) == M:
        value=' '.join(map(str, comb))
        if value not in result:
            result.append(value)
        return
    for i in range(N):
        comb.append(num_lst[i])
        combination()
        comb.pop()
combination()
for i in result:
    print(i)