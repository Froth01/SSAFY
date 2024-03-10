def maze_check(y,x,length):
    queue = []
    queue.append([y,x,length])
    visited[y][x]=1
    while queue:
        q = queue.pop(0)
        for d in range(4):
            di = q[0]+dti[d]
            dj = q[1]+dtj[d]
            if di == N-1 and dj == M-1:
                return q[2]+1
            elif di<0 or di>N-1 or dj<0 or dj>M-1:
                continue
            elif visited[di][dj]==0 and frame[di][dj]=='1':
                visited[di][dj]=1
                queue.append([di,dj,q[2]+1])

if __name__ == "__main__":
    N,M = map(int,input().split())
    frame = [list(input()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    print(maze_check(0,0,1))