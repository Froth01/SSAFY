def inorder_traverse(lst,start):
    global put_num
    if start<=N:
        inorder_traverse(lst,2*start)
        put_num+=1
        result[lst[start-1]]=put_num
        inorder_traverse(lst,2*start+1)

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(range(1,N+1))
    put_num = 0
    result = [0]*(N+1)
    inorder_traverse(nums,1)
    print(result)
    print(f'#{t+1} {result[1]} {result[N//2]}')

