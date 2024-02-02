T = int(input())
for t in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    up = 1
    maximum = 1
    for i in range(len(C)-1):
        if C[i]<C[i+1]:
            up+=1
            if maximum<up:
                maximum = up
        else:
            up = 1
    print(f'#{t+1} {maximum}')