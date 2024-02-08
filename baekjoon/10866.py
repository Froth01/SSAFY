import sys
from collections import deque
input = sys.stdin.readline
d=deque()
N = int(input())
for n in range(N):
    word = input().split()
    if word[0]=='push_front':
        d.appendleft(word[1])
    elif word[0]=='push_back':
        d.append(word[1])
    elif word[0]=='pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif word[0]=='pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif word[0]=='size':
        print(len(d))
    elif word[0]=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif word[0]=='front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif word[0]=='back':
        if d:
            print(d[-1])
        else:
            print(-1)