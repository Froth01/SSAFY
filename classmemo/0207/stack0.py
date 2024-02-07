T = int(input())
for t in range(T):
    N = int(input())
    case = list(map(int, input().split()))
    num_lst = [0]*N
    top = -1
    sum_num = 0
    for c in range(len(case)):
        if case[c]==0:
            num_lst[top]=0
            top-=1
        else:
            top+=1
            num_lst[top] = case[c]
    for num in num_lst:
        sum_num+=num
    print(f'#{t+1} {sum_num}')

