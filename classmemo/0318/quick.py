def quick_sort(lst):
    global result
    if len(lst) <= 1:
        return lst
    low, high = [], []
    cnt = 0
    for n in lst:
        if n < lst[0]:
            low.append(n)
        elif n > lst[0]:
            high.append(n)
        else:
            cnt+=1
    return quick_sort(low) + [lst[0]]*cnt + quick_sort(high)

T = int(input())
for t in range(T):
    N = int(input())
    num = list(map(int,input().split()))
    result = quick_sort(num)
    print(f'#{t+1} {result[N//2]}')