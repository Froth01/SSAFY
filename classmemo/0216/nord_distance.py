# def BFS(lst,v,goal):
#     global road,cnt
#     visited = [0]*(V+1)
#     queue = []
#     queue.append(v)
#     while queue:
#         t = queue.pop(0)
#         if t == goal:
#             road = True
#             return visited[t]
#         else:
#             for i in lst[t]:
#                 if not visited[i]:
#                     queue.append(i)
#                     visited[i] = visited[t]+1
#
# T = int(input())
# for t in range(T):
#     V,E=map(int,input().split())
#     adjl = [[] for _ in range(V+1)]
#     for i in range(E):
#         n1,n2 = map(int,input().split())
#         adjl[n1].append(n2)
#         adjl[n2].append(n1)
#     S,G = map(int,input().split())
#     road = False
#     result = BFS(adjl, S, G)
#     if road:
#         print(f"#{t+1} {result}")
#     else:
#         print(f"#{t+1} 0")
s = []
ss = [[]]
sss = [[],[],[]]
if s:
    print(s)
else:
    print(0)
if sss:
    print(sss)
else:
    print(000)
if ss:
    print(ss)
else:
    print(00)