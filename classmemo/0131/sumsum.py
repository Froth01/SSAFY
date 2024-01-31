A = list(range(1,13))
T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    result = 0
    for i in range(1<<len(A)):
        sum_num = 0
        count = 0
        for j in range(len(A)):
            if i&(1<<j):
                sum_num+=A[j]
                count+=1
        if sum_num==K and count==N:
            result+=1
    print(f'#{t+1} {result}')