A = list(map(int,range(1,13)))
T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    cnt = 0
    subsets = []

    def backtrack(start, path):
        if len(path) == N:
            subsets.append(path)
            return
        for i in range(start, len(A)):
            backtrack(i + 1, path + [A[i]])

    backtrack(0, [])
    for n in subsets:
        if sum(n)==K:
            cnt+=1
    print(f'#{t+1} {cnt}')