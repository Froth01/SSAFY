import sys
input = sys.stdin.readline

N,M = map(int, input().split())
num_lst = list(map(int,input().split()))
num_lst.sort()
visited = [False]*N
comb = []
result = []
def combination():
    if len(comb) == M:
        print(' '.join(map(str, comb)))
        return
    repeat = 0
    for i in range(N):
        if not visited[i] and repeat != num_lst[i]:
            visited[i] = True
            comb.append(num_lst[i])
            repeat = num_lst[i]
            combination()
            comb.pop()
            visited[i] = False
combination()
for i in result:
    print(i)