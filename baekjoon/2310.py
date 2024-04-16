import sys
input = sys.stdin.readline

def adventure(start,money,visit):
    global escape
    if escape:
        return
    visit[start] = 1
    if events[start][0] == 'T':
        if money < events[start][1]:
            return
        elif start == N:
            escape = True
            return
        money -= events[start][1]
        for to in maze[start]:
            if not visit[to]:
                adventure(to,money,visit)
                visit[to]=0
    elif start == N:
        escape = True
        return
    else :
        if money < events[start][1]:
            money = events[start][1]
        for to in maze[start]:
            if not visit[to]:
                adventure(to, money, visit)
                visit[to] = 0

while True:
    N = int(input())
    if N == 0:
        exit()
    maze = [[] for _ in range(N+1)]
    events = ['-']*(N+1)
    visited = [0]*(N+1)
    escape = False
    for n in range(1,N+1):
        event,set,*next,end = input().split()
        events[n] = [event,int(set)]
        for room in next:
            maze[n].append(int(room))
    adventure(1,0,visited)
    if escape:
        print('Yes')
    else:
        print('No')



