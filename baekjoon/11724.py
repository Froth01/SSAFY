import sys
from collections import deque
input = sys.stdin.readline

def circle(start,graph,visited):
    queue = deque()
    queue.append(start)
    while queue:
        q = queue.popleft()
        visited[q]=1
        for to in graph[q]:
            if visited[to]:
                continue
            else:
                queue.append(to)

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
cnt = 0
for n in range(1,len(visited)):
    if not visited[n]:
        circle(n,graph,visited)
        cnt+=1
print(cnt)