import sys
input = sys.stdin.readline

def zip(n,y,x):
    print('(', end='')
    # 좌상단
    trigger = False
    for i in range(y,N//2**n):
        for j in range(x,N//2**n):
            if frame[i][j] != frame[y][x]:
                trigger = True
                zip(n+1,y,x)
                break
    if not trigger:
        print(f'{frame[y][x]}', end='')
    # 우상단
    trigger = False
    for i in range(y,N//2**n):
        for j in range((N//2**n)+x,N):
            if frame[i][j] != frame[y][(N//2**n)+x]:
                trigger = True
                zip(n+1,y,(N//2**n)+x)
                break
    if not trigger:
        print(f'{frame[y][(N//2**n)+x]}', end='')
    # 좌하단
    trigger = False
    for i in range((N//2**n)+y,N//2**n):
        for j in range(x,N):
            if frame[i][j] != frame[(N//2**n)+y][x]:
                trigger = True
                zip(n+1,(N//2**n)+y,x)
                break
    if not trigger:
        print(f'{frame[(N//2**n)+y][x]}', end='')
    # 우하단
    trigger = False
    for i in range((N//2**n)+y,N):
        for j in range((N//2**n)+x,N):
            if frame[i][j] != frame[(N//2**n)+y][(N//2**n)+x]:
                trigger = True
                zip(n+1,(N//2**n)+y,(N//2**n)+x)
                break
    if not trigger:
        print(f'{frame[(N//2**n)+y][(N//2**n)+x]}', end='')
    print(')', end='')

N = int(input())
frame = [list(input()) for _ in range(N)]
zip(1,0,0)


