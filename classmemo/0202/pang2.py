T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    field = [list(map(int,input().split())) for _ in range(N)]
############
    max_v = 0
    dti = [0, 1, 0, -1]
    dtj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            cnt = field[i][j]
            for d in range(4):
                di = i+dti[d]
                dj = j+dtj[d]
                if 0<=di<N and 0<=dj<M:
                    cnt+=field[di][dj]
            if max_v < cnt:
                max_v=cnt
    print(f'#{t+1} {max_v}')

