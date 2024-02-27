import sys
input = sys.stdin.readline

garo,sero = map(int,input().split())
N = int(input())
shop_lst = []
for n in range(N):
    shop_lst.append(list(map(int,input().split())))
donggeun = list(map(int,input().split()))
distance = [[] for _ in range(4)]
for i in range(2):
    for g in range(1,garo):
        if donggeun[0]==i:
            distance[i].append(abs(donggeun[1]-g))
        else:
            if garo-g<=donggeun[1]:
                distance[i].append(donggeun[1]+g+sero)
            else:
                distance[i].append(garo-donggeun[1]+garo-g+sero)
for i in range(2):
    for s in range(1,sero):
        if donggeun[0]==i:
            distance[i].append(abs(donggeun[1]-s))
        else:
            if sero-g<=donggeun[1]:
                distance[i].append(donggeun[1]+s+garo)
            else:
                distance[i].append(sero-donggeun[1]+sero-s+garo)
dis_sum = 0
for shop in shop_lst:
    dis_sum+=distance[shop[0]][shop[1]]
print(dis_sum)


