import sys
input = sys.stdin.readline

def path_length(y,x,length):
    queue = []
    queue.append([y,x,length])
    visited[y][x]=1
    frame[y][x] = 0
    while queue:
        q = queue.pop(0)
        for d in range(4):
            di = q[0]+dti[d]
            dj = q[1]+dtj[d]
            if di<0 or di>N-1 or dj<0 or dj>M-1:
                continue
            elif visited[di][dj]==0 and frame[di][dj]==1:
                visited[di][dj]=1
                frame[di][dj]=q[2]
                queue.append([di,dj,q[2]+1])

if __name__=="__main__":
    N,M = map(int,input().split())
    frame = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    for i in range(N):
        for j in range(M):
            if frame[i][j]==2:
                path_length(i,j,1)
                for ii in range(N):
                    for jj in range(M):
                        if frame[ii][jj]==1 and visited[ii][jj]==0:
                            frame[ii][jj]=-1
                for f in frame:
                    print(*f)
                exit()