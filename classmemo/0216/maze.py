def BFS(lst,v):
    global road
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        for d in range(4):
            di = t[0]+dti[d]
            dj = t[1]+dtj[d]
            if 0>di or di>N-1 or 0>dj or dj>N-1:
                continue
            elif lst[di][dj]==0:
                if not visited[di][dj]:
                    queue.append([di,dj])
                    visited[di][dj] = visited[t[0]][t[1]]+1
            elif lst[di][dj]==3:
                road = True
                return visited[t[0]][t[1]]

T = int(input())
for t in range(T):
    N = int(input())
    maze=[list(map(int,input())) for _ in range(N)]
    start = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                start = [i,j]
    dti = [1,-1,0,0]
    dtj = [0,0,1,-1]
    road = False
    result = BFS(maze,start)
    if road:
        print(f'#{t+1} {result}')
    else:
        print(f'#{t+1} 0')