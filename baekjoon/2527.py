import sys
input = sys.stdin.readline

# def search(square):
#     result = ['d', 'c', 'b', 'a']
#     meet_x = 0
#     meet_y = 0
#     trigger_x = 0
#     trigger_y = 0
#     yes = False
#     #square [ 1시작x,1시작y,1끝x,1끝y,2시작x,2시작y,2끝x,2끝y ]
#     for n in range(square[4],square[6]+1):
#         if n in range(square[0],square[2]+1):
#             if yes:
#                 trigger_x = 1
#                 break
#             meet_x = 1
#             yes = True
#     yes = False
#     for n in range(square[5],square[7]+1):
#         if n in range(square[1],square[3]+1):
#             if yes:
#                 trigger_y = 1
#                 break
#             meet_y = 1
#             yes = True
#     return result[(meet_x and meet_y)+trigger_x+trigger_y]

for n in range(4):
    x1,y1,xx1,yy1,x2,y2,xx2,yy2 = list(map(int,input().split()))
    if (x1==xx2 and y1==yy2) or (xx1==x2 and y1==yy2) or \
        (x1==xx2 and yy1==y2) or (xx1==x2 and yy1==y2):
        print('c')
    elif xx2<x1 or xx1<x2 or yy2<y1 or yy1<y2:
        print('d')
    elif x1==xx2 or xx1==x2 or y1==yy2 or yy1==y2:
        print('b')
    else:
        print('a')

