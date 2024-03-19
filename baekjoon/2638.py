import sys
input = sys.stdin.readline


N,M = map(int,input().split())
frame = [list(map(int,input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
dti = [0,1,0,-1]
dtj = [1,0,-1,0]
trigger = False

def dfs_wall(i,j):
    queue = []
    queue.append([i,j])
    visited[i][j] = 1
    frame[i][j] = 3 #외부 3
    while queue:
        q = queue.pop()
        for d in range(4):
            di = q[0] + dti[d]
            dj = q[1] + dtj[d]
            if di<0 or di>N-1 or dj<0 or dj>M-1:
                continue
            elif not visited[di][dj] and frame[di][dj]==0:
                visited[di][dj] = 1
                frame[di][dj] = 3
                queue.append([di,dj])

def melt_check(i,j):
    global trigger
    cnt = 0
    for d in range(4):
        di = i + dti[d]
        dj = j + dtj[d]
        if di < 0 or di > N - 1 or dj < 0 or dj > M - 1:
            continue
        elif frame[di][dj] == 3:
            cnt+=1
            visited[i][j] = 1
    if cnt >= 2:
        visited[i][j]+=1
    if i == N-1 and j == M-1:
        trigger = True

def hour_go():

    for i in range(N):
        for j in range(M):
            if visited[i][j]>1:
                frame[i][j] = 3

def air_go():
    for i in range(N):
        for j in range(M):
            if frame[i][j] == 0:
                for d in range(4):
                    di = i + dti[d]
                    dj = j + dtj[d]
                    if di < 0 or di > N - 1 or dj < 0 or dj > M - 1:
                        continue
                    elif frame[di][dj] == 3:
                        frame[i][j] = 3

dfs_wall(0,0)
turn = 1
while True:
    flag = False
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                flag = True
                melt_check(i,j)
                if trigger:
                    hour_go()
                    air_go()
                    break
        if flag:
            break
    if not flag:
        break
print(turn)