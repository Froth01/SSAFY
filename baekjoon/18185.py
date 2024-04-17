import sys
input = sys.stdin.readline

N = int(input())
need = list(map(int,input().split())) + [0,0]
cost = 0
for fac in range(len(need)-2):
    if need[fac+1] > need[fac+2]:
        buy = min(need[fac],need[fac+1]-need[fac+2])
        need[fac] -= buy
        need[fac+1] -= buy
        cost += 5 * buy
        buy = min(need[fac:fac+3])
        need[fac] -= buy
        need[fac + 1] -= buy
        need[fac + 2] -= buy
        cost += 7 * buy
        cost += 3 * need[fac]
    else :
        buy = min(need[fac:fac + 3])
        need[fac] -= buy
        need[fac + 1] -= buy
        need[fac + 2] -= buy
        cost += 7 * buy
        buy = min(need[fac:fac+2])
        need[fac] -= buy
        need[fac + 1] -= buy
        cost += 5 * buy
        cost += 3 * need[fac]
print(cost)