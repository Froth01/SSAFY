from heapq import heappop,heappush

a = []
heappush(a,[1,5])
heappush(a,[1,3])

while a:
    print(heappop(a))