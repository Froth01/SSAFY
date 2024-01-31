T=int(input())
for t in range(T):
    N = int(input())
    sum_num = 0
    frame = []
    for n in range(N):
        frame.append(list(map(int,input().split())))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ki = i+di[k]
                kj = j+dj[k]
                if ki>4 or kj>4 or ki<0 or kj<0 :
                    continue
                sum_num+=abs(frame[i][j]-frame[ki][kj])
    print(f'#{t+1} {sum_num}')



