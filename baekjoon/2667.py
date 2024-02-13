import sys
input = sys.stdin.readline

def dfs(x,y):
    global cnt,homes
    for d in range(4):
        di = x + dti[d]
        dj = y + dtj[d]
        if 0>di or di>N-1 or 0>dj or dj>N-1:
            continue
        elif frame[di][dj] == '1' and visited[di][dj] == 0:
            visited[di][dj] = 1
            homes[cnt]+=1
            dfs(di, dj)

N = int(input())
frame = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dti = [0,1,0,-1]
dtj = [1,0,-1,0]
cnt = 0
homes = []
for i in range(N):
    for j in range(N):
        if frame[i][j]=='1' and visited[i][j]==0:
            visited[i][j]=1
            homes.append(1)
            dfs(i,j)
            cnt+=1
homes.sort()
print(cnt)
for home in homes:
    print(home)