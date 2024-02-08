import sys
from collections import deque
input = sys.stdin.readline
queue=deque()
N = int(input())
for n in range(N):
    word = input().split()
    if word[0]=='push':
        queue.append(int(word[1]))
    elif word[0]=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif word[0]=='size':
        print(len(queue))
    elif word[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif word[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif word[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
