def service_check(grade,)


T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            for K in range(1,N+1):
                cnt = 0
                visited = [[0]*N for _ in range(N)]
                service_check(1,K)