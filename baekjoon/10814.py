N = int(input())
count=[0]*201
member = [input().split() for _ in range(N)]
for n in member:
    count[int(n[0])]=n


s=[(20,30),(40,50)]
s[1]+=(20,30)
print(s)















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
