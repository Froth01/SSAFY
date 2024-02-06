def de_sum(num):
    each = list(map(int,str(num)))
    return num+sum(each)

N = int(input())
if N<18:
    minus_range = N
else:
    minus_range = 9 * len(str(N))
result = False
for m in range(minus_range,0,-1):
    if de_sum(N-m)==N:
        print(N-m)
        result = False
        break
    else:
        result = True
        continue
if result:
    print(0)