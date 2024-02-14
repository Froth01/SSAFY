import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
low = 0
high = max(tree)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = 0
    for t in tree:
        if t > mid:
            total += t - mid
    if total >= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1
print(result)