# 도전 친구와 카페 방문
# all = ['A','B','C','D','E']
# get = [False for _ in range(len(all))]
# together = []
#
#
# def friend(x):
#     if x==2:
#         print(*together)
#         return
#     for i in range(5):
#         if get[i]:
#             continue
#         get[i] = True
#         together.append(all[i])
#         friend(x+1)
#         together.pop()
#         get[i] = False
#
# friend(0)
#
# 바이너리 체크
# arr = ['A','B','C','D','E']
# n = len(arr)
#
# def get_count(tar):
#     cnt = 0
#     for i in range(n):
#         if tar & 0x1:
#             cnt+=1
#         tar >>= 1
#     return cnt
#
# result = 0
# for tar in range(1 << n):
#     if get_count(tar) >= 2:
#         result +=1
# print(result)

'''
ABC
ABD
ABE
ACD
ACE
ADE
BCD
BCE
BDE
CDE
'''
# # 3주사위 조합
# N = 3
# path = []
# def func(level,start):
#     if level == N:
#         return
#     for i in range(start,7):
#         path.append(i)
#         func(level+1, i)

