import sys
input = sys.stdin.readline
from collections import deque

M,N = map(int,input().split())
frame = [list(map(int,input().split())) for _ in range(N)]
day = 0
welldone = deque()
dti = [0,1,0,-1]
dtj = [1,0,-1,0]

for i in range(N):
    for j in range(M):
        if frame[i][j] == 1:
            welldone.append((i, j))
        elif frame[i][j] == 0:
            possible = False
            for d in range(4):
                di = i + dti[d]
                dj = j + dtj[d]
                if 0 <= di < N and 0 <= dj < M and frame[di][dj] != -1:
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
        i, j = welldone.popleft()
        for d in range(4):
            di = i + dti[d]
            dj = j + dtj[d]
            if 0 <= di < N and 0 <= dj < M and frame[di][dj] == 0:
                frame[di][dj] = 1
                welldone.append((di, dj))
                done = 1
    day += done
for line in frame:
    if 0 in line:
        print(-1)
        exit()
print(day)