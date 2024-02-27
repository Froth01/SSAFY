def route(x,y,sum_val):
    global min_val
    if sum_val>min_val:
        return
    elif 0>x or x>N-1 or 0>y or y>N-1:
        return
    elif x==N-1 and y==N-1:
        sum_val+=frame[x][y]
        if min_val>sum_val:
            min_val=sum_val
        return
    for i in range(1,3):
        sum_val+=frame[x][y]
        route(x+(i//2),y+i%2,sum_val)
        sum_val-=frame[x][y]


T = int(input())
for t in range(T):
    N = int(input())
    frame = [list(map(int,input().split())) for _ in range(N)]
    min_val = 9999999
    route(0,0,0)
    print(f'#{t+1} {min_val}')