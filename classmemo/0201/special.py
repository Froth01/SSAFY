def selection(lst):
    for n in range(len(lst)):
        mini = 99999
        for m in range(n,len(lst)):
            if lst[m]<mini:
                mini = lst[m]
                min_idx = m
        lst[n],lst[min_idx]=lst[min_idx],lst[n]
    return lst

T = int(input())
for t in range(T):
    N = int(input())
    ai = list(map(int,input().split()))
    selection(ai)
    result = []
    for n in range(5):
        result.append(ai[-n-1])
        result.append(ai[n])


    print(f'#{t+1}',end=' ')
    print(*result)