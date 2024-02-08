import sys
input = sys.stdin.readline
from collections import deque

M,N,H = map(int,input().split())
frame = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
day = 0
welldone = deque()
dti = [0,1,0,-1,0,0]
dtj = [1,0,-1,0,0,0]
dth = [0,0,0,0,1,-1]
for h in range(H):
    for i in range(N):
        for j in range(M):
            if frame[h][i][j] == 1:
                welldone.append((h, i, j))
            elif frame[h][i][j] == 0:
                possible = False
                for d in range(6):
                    dh = h + dth[d]
                    di = i + dti[d]
                    dj = j + dtj[d]
                    if 0<= dh < H and 0 <= di < N and 0 <= dj < M and frame[dh][di][dj] != -1:
                        possible = True
                        break
                if not possible:
                    print(-1)
                    exit()

if not welldone:
    print(-1)
    exit()

while welldone:
    job = len(welldone)
    done = 0
    for _ in range(job):
        h, i, j = welldone.popleft()
        for d in range(6):
            dh = h + dth[d]
            di = i + dti[d]
            dj = j + dtj[d]
            if 0<= dh < H and 0 <= di < N and 0 <= dj < M and frame[dh][di][dj] == 0:
                frame[dh][di][dj] = 1
                welldone.append((dh, di, dj))
                done = 1
    day += done
for high in frame:
    for line in high:
        if 0 in line:
            print(-1)
            exit()
print(day)