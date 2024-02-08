import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
people = deque(x for x in range(1,N+1))
result = []
while people:
    people.rotate(-(K-1))
    result.append(people.popleft())
print('<',end='')
print(*result,sep=', ',end='')
print('>')
