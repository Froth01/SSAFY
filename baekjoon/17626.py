import math
def rootminus(num,lst):
    if num == 0:
        return
    elif num == 1:
        lst.append(1)
        return
    else:
        minus = int(math.sqrt(num))
        lst.append(minus)
        rootminus(num-minus**2,lst)

N = int(input())
check = []
rootminus(N,check)
print(len(check))