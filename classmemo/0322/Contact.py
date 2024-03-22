def call_emer(start):
    global cnt
    queue = []
    queue.append(start)
    visited[start]=1
    while queue:
        q = queue.pop(0)
        for g in graph[q]:
            if visited[g]:
                continue
            else:
                visited[g] = cnt = visited[q]+1
                queue.append(g)


for t in range(10):
    data, start = map(int,input().split())
    info = list(map(int,input().split()))
    graph = [[] for _ in range(101)]
    visited = [0]*101
    cnt = 0
    for i in range(data//2):
        if info[2*i+1] not in graph[info[2*i]]:
            graph[info[2*i]].append(info[2*i+1])
    call_emer(start)
    last = 0
    for v in range(1,101):
        if visited[v]==cnt:
            last = v
    print(f'#{t+1} {last}')