T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    frame = []
    for n in range(N):
        frame.append(list(map(int,input().split())))
########## 입력
    blank = []
    for i in range(N):
        r_cnt=0
        for j in range(N):
            if frame[i][j]==1:
                r_cnt+=1
                if j==N-1:
                    blank.append(r_cnt)
            elif frame[i][j]==0:
                blank.append(r_cnt)
                r_cnt=0
    for j in range(N):
        c_cnt=0
        for i in range(N):
            if frame[i][j]==1:
                c_cnt+=1
                if i==N-1:
                    blank.append(c_cnt)
            elif frame[i][j]==0:
                blank.append(c_cnt)
                c_cnt=0
    result = blank.count(K)
    print(f'#{t+1} {result}')