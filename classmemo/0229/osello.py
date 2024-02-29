def flip(y,x,color):
    frame[y][x]=color
    for d in range(8):
        stack = []
        for g in range(1,N):
            di = y + dti[d]*g
            dj = x + dtj[d]*g
            if 1<=di<N+1 and 1<=dj<N+1:
                if frame[di][dj]==0:
                    break
                elif frame[di][dj]==color:
                    while stack:
                        ni,nj = stack.pop()
                        frame[ni][nj]=color
                    break
                else:
                    stack.append([di,dj])
            else:
                break

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    frame = [[0]*(N+1) for _ in range(N+1)]
    frame[N//2+1][N//2+1]=frame[N//2][N//2]=2
    frame[N//2+1][N//2]=frame[N//2][N//2+1]=1
    dti = [0, 1, 1, 1, 0, -1, -1, -1]
    dtj = [1, 1, 0, -1, -1, -1, 0, 1]
    for m in range(M):
        x,y,color = map(int,input().split())
        flip(y,x,color)
    result = [0,0]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if frame[i][j]==1:
                result[0]+=1
            elif frame[i][j]==2:
                result[1]+=1
    print(f'#{t+1}',end=' ')
    print(*result)