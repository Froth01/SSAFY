N,M = map(int,input().split())
nums = list(map(int,input().split()))
sum_num=[0]
sum_val =0
for n in range(N):
    sum_val+=nums[n]
    sum_num.append(sum_val)
cnt = 0
for n in range(N):
    for m in range(n,N):
        if (sum_num[m]-sum_num[n-1])%M==0:
            cnt+=1
print(cnt)