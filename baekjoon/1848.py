import sys
from heapq import heappush,heappop
input = sys.stdin.readline

def dijkstra_make(start):
    distance = [inf] * N
    pq = []
    heappush(pq,(0,start))
    while pq :
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
            heappush(pq,(new_dist,next_node))

N,M = map(int,input().split())
inf = int(1e9)
graph = [[] for _ in range(N)]

for _ in range(M):
    s,e,t1,t2 = map(int,input().split())
    graph[s-1].append([t1,e-1])
    graph[e-1].append([t2,s-1])

dijkstra = []

print(min_val)