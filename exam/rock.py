def find_path(y,x,dis):
    global visited, min_level
    queue = []
    queue.append([y,x,0])
    visited[y][x] = 1
    trigger = False
    while queue:
        q = queue.pop(0)
        if frame[q[0]][q[1]] == 3:
            trigger = True
            if min_level > q[2]:
                min_level = q[2]
            continue
        for d in range(4):
            for n in range(1,dis):
                di = q[0] + dti[d]*n
                dj = q[1] + dtj[d]
                if di < 0 or di>N-1 or dj<0 or dj>M-1:
                    continue
                elif (visited[di][dj]==0 and frame[di][dj]==1) or frame[di][dj]==3:
                    visited[di][dj]=1
                    if di<y:
                        if q[2]<n:
                            queue.append([di,dj,n])
                        else:
                            queue.append([di,dj,q[2]])
                        break
                    else:
                        queue.append([di,dj,q[2]])
    if not trigger:
        visited = [[0] * M for _ in range(N)]
        find_path(y,x,dis+1)

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    frame = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    min_level = 999999999999
    find_path(N-1,0,2)
    print(f'#{t+1} {min_level}')