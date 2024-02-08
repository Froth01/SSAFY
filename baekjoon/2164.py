import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
card = deque(x for x in range(1,N+1))
while len(card)>1:
    card.popleft()
    card.rotate(-1)
print(*card)