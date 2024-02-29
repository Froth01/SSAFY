T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    frame = [list(map(int,input().split())) for _ in range(N)]
    dti = [[0,1,0,-1],[1,1,-1,-1]]
    dtj = [[1,0,-1,0],[1,-1,-1,1]]
    max_kill = 0
    for i in range(N):
        for j in range(N):
            for n in range(2):
                kill = frame[i][j]
                for d in range(4):
                    for m in range(1,M):
                        di = i + dti[n][d]*m
                        dj = j + dtj[n][d]*m
                        if 0<=di<N and 0<=dj<N:
                            kill+=frame[di][dj]
                if max_kill<kill:
                    max_kill=kill
    print(f'#{t+1} {max_kill}')
