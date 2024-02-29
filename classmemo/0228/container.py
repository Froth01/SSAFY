T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    result = 0
    while truck and container:
            if truck[0]>=container[0]:
                result+=container.pop(0)
                truck.pop(0)
            elif truck[0]<container[0]:
                container.pop(0)
    print(f'#{t+1} {result}')