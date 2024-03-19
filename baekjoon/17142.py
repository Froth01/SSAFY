from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def bfs(virus):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for i, j in virus:
        q.append((i,j))
        visited[i][j] = 0

    answer = 0
    while q:
        i, j = q.popleft()
        for d in range(4):
            di = i + dti[d]
            dj = j + dtj[d]
            if 0 <= di < N and 0 <= dj < N:
                if not frame[di][dj] and visited[di][dj] == -1:
                    q.append((di, dj))
                    visited[di][dj] = visited[i][j] + 1
                    answer = max(answer, visited[di][dj])
                elif frame[di][dj] == 2 and visited[di][dj] == -1:
                    q.append((di, dj))
                    visited[di][dj] = visited[i][j] + 1
    res = 0
    for line in visited:
        res += line.count(-1)
    if res == check:
        return answer
    return 9999999999

N, M = map(int, input().split())
frame = [list(map(int, input().split())) for _ in range(N)]
dti = [-1,1,0,0]
dtj = [0,0,-1,1]
check, viruses = 0, []
for i in range(N):
    for j in range(N):
        if frame[i][j] == 2:
            viruses.append((i,j))
        elif frame[i][j] == 1:
            check += 1

virus_lst = list(combinations(viruses, M))
answer = 9999999999
for virus in virus_lst:
    answer = min(answer, bfs(virus))

if answer == 9999999999:
    print(-1)
else:
    print(answer)