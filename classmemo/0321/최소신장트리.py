from heapq import heappush,heappop

def prim(start):
    pq = []
    MST = [0]*(V+1)
    sum_weight = 0
    heappush(pq,(0,start))
    while pq:
        weight, now = heappop(pq)
        if MST[now]:
            continue
        MST[now] = 1
        sum_weight += weight
        for to in range(V+1):
            if MST[to]:
                continue
            for route in graph[now]:
                if route[1]==to:
                    heappush(pq,(route[0],to))
    print(f'#{t+1} {sum_weight}')


T = int(input())
for t in range(T):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append([w,e])
        graph[e].append([w,s])
    prim(0)
