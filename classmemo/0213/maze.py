def dfs(x,y):
    global clear
    for d in range(4):
        di = x + dti[d]
        dj = y + dtj[d]
        if 0>di or di>N-1 or 0>dj or dj>N-1:
            continue
        elif maze[di][dj]=='0' and visited[di][dj]==0:
            visited[di][dj]=1
            dfs(di,dj)
        elif maze[di][dj]=='3':
            clear = True
            break
T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    clear = False
    start = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                start = i,j
                break
    dfs(start[0],start[1])
    if clear :
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')





