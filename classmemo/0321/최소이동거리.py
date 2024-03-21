from heapq import heappush,heappop

def dijkstra(start):
    pq = []
    heappush(pq,(0,start))
    distance[start]=0
    while pq:
        dist, now = heappop(pq)
        if dist > distance[now]:
            continue
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]
            new_dist = dist + next_dist
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist
            heappush(pq,(new_dist,next_node))



inf = int(1e9)
T = int(input())
for t in range(T):
    N,E = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    distance = [inf]*(N+1)
    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append([w,e])
    dijkstra(0)
    print(f'#{t+1} {distance[-1]}')