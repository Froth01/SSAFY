from heapq import heappush,heappop

def gogo(i,j):
    global fuel
    queue = []
    queue.append([i,j])
    while queue:
        q = queue.pop(0)
        if q[0]==N-1 and q[1]==N-1:
            break
        small = []
        for d in range(2):
            di = q[0] + dti[d]
            dj = q[1] + dtj[d]
            if di<0 or di>N-1 or dj<0 or dj>N-1:
                continue
            heappush(small,(1+abs(frame[q[0]][q[1]]-frame[di][dj]),di,dj))
        way = small[0]
        for route in small:
            route[0]
        queue.append(way[1:])
        fuel += way[0]

T = int(input())
for t in range(T):
    N = int(input())
    frame = [list(map(int,input().split())) for _ in range(N)]
    dti = [0,1]
    dtj = [1,0]
    fuel = 0
    gogo(0,0)
    print(f'#{t+1} {fuel}')