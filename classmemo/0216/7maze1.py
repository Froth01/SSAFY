def BFS(lst,v):
    global road
    visited = [[0]*16 for _ in range(16)]
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        for d in range(4):
            di = t[0]+dti[d]
            dj = t[1]+dtj[d]
            if 0>di or di>15 or 0>dj or dj>15:
                continue
            elif lst[di][dj]==0:
                if not visited[di][dj]:
                    visited[di][dj]=1
                    queue.append([di,dj])
            elif lst[di][dj]==3:
                road = True
                return 1
    return 0

for t in range(10):
    tc = int(input())
    maze=[list(map(int,input())) for _ in range(16)]
    start = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                start = [i,j]
    dti = [1,-1,0,0]
    dtj = [0,0,1,-1]
    road = False
    BFS(maze,start)
    if road:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')