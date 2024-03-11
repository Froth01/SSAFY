T = int(input())
for t in range(T):
    N = int(input())
    frame = [input().rstrip() for _ in range(N)]
    dti = [1,1,1,0,-1]
    dtj = [-1,0,1,1,1]
    result = 'NO'
    trigger = False
    for i in range(N):
        for j in range(N):
            if frame[i][j]=='o':
                for d in range(5):
                    cnt = 1
                    g = 1
                    di = i + dti[d]
                    dj = j + dtj[d]
                    while 0<=di<N and 0<=dj<N:
                        if cnt>=5:
                            result = 'YES'
                            trigger = True
                            break
                        elif frame[di][dj]=='o':
                            cnt+=1
                        elif cnt>=1 and frame[di][dj]!='o':
                            cnt=0
                        di+=dti[d]
                        dj+=dtj[d]
                        g+=1
                    if cnt>=5:
                        result='YES'
                        trigger = True
                        break
            elif trigger:
                break
        if trigger:
            break
    print(f'#{t+1} {result}')