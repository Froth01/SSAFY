def heap_push(n,m):
    heap.append(n)
    while heap[m]<heap[m//2]:
        heap[m],heap[m//2]=heap[m//2],heap[m]
        m//=2
        if m==0:
            break

T = int(input())
for t in range(T):
    N = int(input())
    nums = [0]+list(map(int,input().split()))
    heap = [0, nums[1]]
    for i in range(2,N+1):
        heap_push(nums[i],i)
    result = 0
    while N!=0:
        N//=2
        result+=heap[N]
    print(f'#{t+1} {result}')
