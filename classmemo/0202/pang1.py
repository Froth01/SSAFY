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
                for x in range(1,field[i][j]+1):
                    di = i+(dti[d]*x)
                    dj = j+(dtj[d]*x)
                    if 0<=di<N and 0<=dj<M:
                        cnt+=field[di][dj]
            if max_v < cnt:
                max_v=cnt
    print(f'#{t+1} {max_v}')