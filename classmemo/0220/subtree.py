def subtree_search(num):
    global cnt
    cnt+=1
    if adjl[num]:
        for n in adjl[num]:
            subtree_search(n)

T = int(input())
for t in range(T):
    E,N = map(int,input().split())
    line_lst = list(map(int,input().split()))
    adjl = [[] for _ in range(E+2)]
    cnt = 0
    for e in range(0,len(line_lst)//2):
        n1 = line_lst[2*e]
        n2 = line_lst[2*e+1]
        adjl[n1].append(n2)
    subtree_search(N)
    print(f'#{t+1} {cnt}')