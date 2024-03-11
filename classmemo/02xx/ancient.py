T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    frame = [list(map(int,input().split())) for _ in range(N)]
    max_length = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if frame[i][j]!=0:
                cnt+=1
            elif cnt>0 and frame[i][j]==0:
                if max_length<cnt:
                    max_length=cnt
                cnt = 0
        if max_length<cnt:
            max_length=cnt
    for j in range(M):
        cnt = 0
        for i in range(N):
            if frame[i][j]!=0:
                cnt+=1
            elif cnt>0 and frame[i][j]==0:
                if max_length<cnt:
                    max_length=cnt
                cnt = 0
        if max_length<cnt:
            max_length=cnt
    print(f'#{t+1} {max_length}')