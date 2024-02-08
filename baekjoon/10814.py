import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
members=deque()
count = [0]*201
for n in range(N):
    member=input().split()
    if len(members)==0:
        members.append(member)
        count[int(member[0])]+=1
    elif int(member[0])<int(members[-1][0]):
        seat = sum(count[:int(member[0])+1])
        members.insert(seat,member)
        count[int(member[0])] += 1
    else:
        members.append(member)
        count[int(member[0])]+=1
for p in range(N):
    result = members.popleft()
    print(*result)




















# stack = []
# top = -1
#     if top==-1:
#         top+=1
#         stack.append(info)
#     elif int(info[0])>=int(stack[top][0]):
#         info, stack[top] = stack[top], info
#         for t in range(top-1,-1,-1):
#             if int(stack[top][0])<int(stack[t][0]):
#                 stack[top], stack[t] = stack[t], stack[top]
#         stack.append(info)
#         top+=1
#     else:
#         top+=1
#         stack.append(info)
# for i in range(len(stack)):
#     result = stack.pop()
#     print(*result)
