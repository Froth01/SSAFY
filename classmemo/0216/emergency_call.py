def BFS(lst,v):
    visited = [0]*(101)
    queue = []
    queue.append(v)
    result = []
    while queue:
        t = queue.pop(0)
        for i in lst[t]:
            if not i:
                continue
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    for v in range(len(visited)):
        if visited[v] == max(visited):
            result.append(v)
    return max(result)

for t in range(10):
    man,start = map(int,input().split())
    call_lst = list(map(int,input().split()))
    adjl = [[] for _ in range(101)]
    for i in range(len(call_lst)//2):
        n1,n2 = call_lst[i*2],call_lst[i*2+1]
        adjl[n1].append(n2)
    answer = BFS(adjl,start)
    print(f'#{t+1} {answer}')