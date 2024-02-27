def Per(x,y):
    global path
    if x==y:
        route.append(path)
        return
    for i in range(y):
        if visited[i]:
            continue
        visited[i]=True
        path+=str(i)
        Per(x+1,y)
        path=path[:-1]
        visited[i]=False




T = int(input())
for t in range(T):
    N = int(input())
    frame = [list(map(int,input().split())) for _ in range(N)]
    route = []
    visited = [False for _ in range(N)]
    path=''
    Per(0,N)
    max_score = 0
    for r in route:
        score = 0
        for i in range(N):
            score+=frame[i][int(r[i])]
        if max_score<score:
            max_score=score
    print(f'#{t+1} {max_score}')