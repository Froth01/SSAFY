def merge_sort(lst):
    global cnt

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])

    i=j=0
    result = []
    if l[-1]>r[-1]:
        cnt+=1
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    if i < len(l):
        result.extend(l[i:])
    else:
        result.extend(r[j:])
    return result

T = int(input())
for t in range(T):
    N = int(input())
    num = list(map(int,input().split()))
    cnt = 0
    sorted = merge_sort(num)
    if N==1:
        print(f'#{t+1} {num[]}')
    print(f'#{t+1}',end=' ')
    print(sorted[N//2],cnt)
