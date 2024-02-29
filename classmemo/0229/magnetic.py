for t in range(10):
    N = int(input())
    frame = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        trigger = False
        for i in range(N):
            if frame[i][j]==1:
                trigger = True
            elif trigger and frame[i][j]==2:
                cnt+=1
                trigger = False
    print(f'#{t+1} {cnt}')