import sys
from collections import deque
input = sys.stdin.readline

def R():
    global trigger
    if trigger:
        trigger = False
    else:
        trigger = True
    pass

def D(lst):
    global error
    try:
        if trigger:
            lst.pop()
        else:
            lst.popleft()
        return lst
    except:
        error = 1
        pass


T = int(input())
for t in range(T):
    p = input()
    N = int(input())
    source = deque(eval(input()))
    trigger = False
    error = 0
    for work in range(len(p)):
        if p[work]=='R':
            R()
        elif p[work]=='D':
            D(source)
    if error==1:
        print('error')
    elif trigger:
        print('[', end='')
        print(*reversed(source),sep=',',end='')
        print(']')
    else:
        print('[', end='')
        print(*source, sep=',', end='')
        print(']')

