# 재귀
# 1111~3333 까지 수 출력하는 코드 몇중 for문 사용해야하나??
# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             for l in range(1,4):
#                 print(i,j,k,l)

# 함수는 호출했던 곳으로 돌아온다
# def main():
#     KFC(0)
#     print('끝')
#
# def KFC(x):
#     if x==6:
#         return
#     print(x,end=' ')
#     KFC(x+1)
#     print(x,end=' ')
#
# 기저조건은 level, for문 반복 횟수는 branch

# path = []
#
# def KFC(x):
#     if x==2:
#         print(path)
#         return
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)


# 도전문제 중복순열 111~666
# path = []
#
# def KFC(x):
#     if x==3:
#         print(*path)
#         return
#     for i in range(1,7):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)

# 추가 도전 11111~44444
# path = []
#
# def KFC(x):
#     if x==5:
#         print(*path)
#         return
#     for i in range(1,5):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)


#순열 - 구성요소수=branch=for문 range / 순열자릿수=level,기저조건 값
# path = []
# visited = [False for _ in range(6)]
#
# def Per(x,y):
#     if x==y:
#         print(*path)
#         return
#     for i in range(1,y+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         path.append(i)
#         Per(x+1,y)
#         path.pop()
#         visited[i]=False
#
# Per(0,3)


# # 도전 주사위
# def Per(x,y,z):
#     if x==y:
#         print(*path)
#         return
#     for i in range(1,7):
#         if z==2 and visited[i]:
#             continue
#         visited[i]=True
#         path.append(i)
#         Per(x+1,y,z)
#         path.pop()
#         visited[i]=False
#
# N,Type = map(int,input().split())
# visited =[False for _ in range(7)]
# path = []
# Per(0,N,Type)

# 완전탐색 10이하 주사위 눈 누적합

