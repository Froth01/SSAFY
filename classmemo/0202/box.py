T=int(input())
for t in range(T):
    N,Q = map(int,input().split())
    box = [0]*N
    for q in range(1,Q+1):
        L,R = map(int,input().split())
        for x in range(L-1,R):
            box[x]=q
    print(f'#{t+1}',end=' ')
    print(*box)