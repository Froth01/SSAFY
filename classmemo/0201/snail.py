T = int(input())
for t in range(T):
    N = int(input())
    frame = [[0]*N for _ in range(N)]
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    num = 1
    d=0
    i=0
    j=0
    while num<=N**2:
        if 0<=i<=N-1 and 0<=j<=N-1 and frame[i][j]==0:
            frame[i][j]=num
            num+=1
        else:
            i,j = i-dti[d],j-dtj[d]
            d=(d+1)%4

        i,j = i+dti[d],j+dtj[d]

    print(f'#{t+1}')
    for line in frame:
        print(*line)



