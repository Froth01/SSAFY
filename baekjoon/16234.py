def Check_move(y,x,num):
    queue = []
    queue.append([y,x])
    visited[y][x]=1
    together = []
    while queue:
        t = queue.pop(0)
        for d in range(4):
            di = t[0]+dti[d]
            dj = t[1]+dtj[d]
            if di<0 or di>N-1 or dj<0 or dj>N-1:
                continue
            elif visited[di][dj]==0:
                visited[di][dj]=1
                if L<=abs(frame[t[0]][t[1]]-frame[di][dj])<=R:
                    together.append(frame[di][dj])






N,L,R = map(int,input().split())
frame = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dti = [0,1,0,-1]
dtj = [1,0,-1,0]
union = []