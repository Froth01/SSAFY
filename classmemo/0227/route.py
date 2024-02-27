def all_route(x,start,length):
    global min_length
    if length>min_length:
        return
    elif x==N:
        length+=distance[start][1]
        if length<min_length:
            min_length=length
        return
    for i in range(2,N+2):
        if visited[i]:
            continue
        visited[i]=True
        length+=distance[start][i]
        all_route(x+1,i,length)
        length-=distance[start][i]
        visited[i]=False

for t in range(int(input())):
    N = int(input())
    info = list(map(int,input().split()))
    visited = [False for _ in range(N+2)]
    distance = [[] for _ in range(N+2)]
    for i in range(N+2):
        for j in range(0,len(info),2):
            distance[i].append(abs(info[2*i]-info[j])+abs(info[2*i+1]-info[j+1]))
    min_length = 9999999
    all_route(0,0,0)
    print(f'#{t+1} {min_length}')