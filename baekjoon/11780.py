import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = int(1e9)
graph = [[inf] * N for _ in range(N)]
route = [[0]* N for _ in range(N)]
for start in range(N):
    for end in range(N):
        if start == end:
            graph[start][end] = 0
for m in range(M):
    s, e, w = map(int,input().split())
    if graph[s-1][e-1] > w:
        graph[s-1][e-1] = w
for mid in range(N):
    for start in range(N):
        for end in range(N):
            graph[start][end] = min(graph[start][end], graph[start][mid]+graph[mid][end])
for i in range(N):
    for j in range(N):
        if graph[i][j]==inf:
            graph[i][j]=0
for line in range(N):
    print(*graph[line])