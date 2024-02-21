# N = int(input())
# num = list(map(int,input().split()))
# result = []
# for i in range(1<<len(num)):
#     subset = []
#     length = 0
#     for j in range(len(num)):
#         if i & (1<<j):
#             subset.append(num[j])
#             length+=1
#     if length==N and sum(subset)%N==0:
#         result.append(subset)
#         break
# if result:
#     print(*result[0])
# else:
#     print(-1)
import math
print(math.comb(1000,502))
