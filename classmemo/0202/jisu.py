T = int(input())
for t in range(T):
    result = [0,0,0,0,0]
    N = int(input())
    N_low = [11,7,5,3,2]
    while N!=1:
        for n in range(len(N_low)):
            if N%N_low[n]==0:
                N//=N_low[n]
                result[n]+=1
    print(f'#{t+1}',end=' ')
    print(*result[::-1])