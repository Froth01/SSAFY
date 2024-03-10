T = int(input())
for t in range(T):
    N,M1,M2 = map(int,input().split())
    block = list(map(int,input().split()))
    block.sort(reverse=True)
    towers = [[],[]]
    i = 0
    while block:
        if len(towers[0])==M1:
            towers[1].append(block.pop(0))
        elif len(towers[1])==M2:
            towers[0].append(block.pop(0))
        else:
            towers[i%2].append(block.pop(0))
            i+=1
    sum_cost = 0
    for tower in towers:
        for n in range(1,len(tower)+1):
            sum_cost+=n*tower[n-1]
    print(f'#{t+1} {sum_cost}')