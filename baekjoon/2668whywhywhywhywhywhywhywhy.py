import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(i, j, h):
    for d in range(4):
        di = i + dti[d]
        dj = j + dtj[d]
        if di<0 or di>=N or dj<0 or dj>=N:
            continue
        elif not safe_area[di][dj] and frame[di][dj] > h:
            safe_area[di][dj] = True
            DFS(di, dj, h)

N = int(input())
frame = [list(map(int, input().split())) for _ in range(N)]
maximum = []
for f in frame:
    maximum.append(max(f))
highest = max(maximum)
dti = [0,1,0,-1]
dtj = [1,0,-1,0]
max_safe = 1
for s in range(highest):
    safe_area = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if frame[i][j] > s and not safe_area[i][j]:
                cnt += 1
                safe_area[i][j] = True
                DFS(i, j, s)
    if max_safe < cnt:
        max_safe = cnt
print(max_safe)