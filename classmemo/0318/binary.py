def binary_search(lst,n):
    global cnt, left, right
    l,r = 0,len(lst)-1
    m = (l+r)//2
    if len(lst)<=1:
        if n==lst[0]:
            cnt+=1
        return
    elif n == lst[m]:
        cnt+=1
        return
    elif n < lst[m]:
        if left:
            return
        left = True
        binary_search(lst[:m],n)
    elif n > lst[m] :
        if right:
            return
        right = True
        binary_search(lst[m+1:],n)



T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    cnt = 0

    for b in B:
        left = False
        right = False
        binary_search(A,b)
    print(f'#{t+1} {cnt}')