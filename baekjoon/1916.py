import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):
    pq = []
    heappush(pq,(0,start))
    distance[start] = 0
    while pq:
        dist, now = heappop(pq)
        if distance[now] < dist:
            continue
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]
            new_dist = dist + next_dist
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist
            heappush(pq, (new_dist,next_node))

N = int(input())
M = int(input())
inf = int(1e9)
graph = [[] for _ in range(N+1)]
for m in range(M):
    s,e,w = map(int,input().split())
    graph[s].append([w,e])
distance = [inf]*(N+1)
start, end = map(int,input().split())
dijkstra(start)
print(distance[end])




