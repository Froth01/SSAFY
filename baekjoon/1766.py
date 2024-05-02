from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
connect = [0]*(N+1)
queue = []
for m in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    connect[b] += 1
for node in range(1,N+1):
    if connect[node] == 0:
        heappush(queue,node)
answer = []
while queue:
    solve = heappop(queue)
    answer.append(solve)
    for to in graph[solve]:
        connect[to] -= 1
        if not connect[to]:
            heappush(queue,to)
print(*answer)

