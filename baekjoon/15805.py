import sys
input=sys.stdin.readline


N=int(input())
route=list(map(int,input().split()))

visit=set()
visit.add(route[0])
way=[0]*(200001)
way[route[0]]=-1

for i in range(1,N):
    if route[i] not in visit:
        way[route[i]]=route[i-1]
        visit.add(route[i])

print(len(visit))
for i in range(len(visit)):
    print(way[i] , end=" ")