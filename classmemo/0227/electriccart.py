def route(x,y,sum_val):
    global min_val
    if sum_val>min_val:
        return
    elif x==N-1:
        sum_val+=info[y][0]
        if min_val>sum_val:
            min_val=sum_val
            return
    for i in range(N):
        if visited[i] or y==i:
            continue
        visited[i]=True
        sum_val+=info[y][i]
        route(x+1,i,sum_val)
        sum_val-=info[y][i]
        visited[i]=False

T = int(input())
for t in range(T):
    N = int(input())
    info = [list(map(int,input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    visited[0]=True
    min_val = 9999999
    route(0,0,0)
    print(f'#{t+1} {min_val}')