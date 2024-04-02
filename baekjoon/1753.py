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
            new_dist = dist + to[0]
            if new_dist >= distance[to[1]]:
                continue
            distance[to[1]] = new_dist
            heappush(pq,(new_dist,to[1]))

inf = int(1e9)
V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V)]
distance = [inf] * V
for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s-1].append([w,e-1])
dijkstra(K-1)
for n in distance:
    if n==inf:
        print('INF')
    else:
        print(n)