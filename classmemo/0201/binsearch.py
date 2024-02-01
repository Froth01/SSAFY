def binsearch(max_num,key):
    l = 1
    r = max_num
    cnt = 0
    while l<=r:
        c = int((l+r)/2)
        cnt+=1
        if key==c:
            return cnt
        elif c>key:
            r = c
        else :
            l = c
    return cnt


T = int(input())
for t in range(T):
    P,A,B = map(int,input().split())
    num_list = [n+1 for n in range(P)]
    if binsearch(P,A)==binsearch(P,B):
        result = '0'
    elif binsearch(P,A)>binsearch(P,B):
        result = 'B'
    else:
        result = 'A'
    print(f'#{t+1} {result}')
