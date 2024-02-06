T = int(input())
for t in range(T):
    A,B = input().split()
    N,M = len(A),len(B)
    cnt = 0
    s = 0
    while s<=N-M:
        pattern = True
        for j in range(M):
            if A[s+j]!=B[j]:
                pattern = False
                break
        if pattern:
            cnt += 1
            s += M-1
        s += 1
    print(f'#{t+1} {N-(M-1)*cnt}')