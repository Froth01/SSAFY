import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    global cnt
    for d in range(4):
        di = x + dti[d]
        dj = y + dtj[d]
        if 0>di or di>N-1 or 0>dj or dj>M-1:
            continue
        elif frame[di][dj]==1 and visited[di][dj]==0:
            visited[di][dj]=1
            dfs(di,dj)

T = int(input())
for t in range(T):
    M,N,K = map(int,input().split())
    frame = [[0]*M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    cnt = 0
    for k in range(K):
        baechu = list(map(int,input().split()))
        frame[baechu[1]][baechu[0]]=1
    for i in range(N):
        for j in range(M):
            if frame[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                dfs(i,j)
                cnt+=1
    print(cnt)