import sys

def fac(num):
    nf = num
    if num == 0:
        return 1
    for n in range(1, num):
        nf = nf * (num - n)
    return nf

def ncr(n, r):
    return fac(n) // (fac(n - r) * fac(r))

N = int(sys.stdin.readlines())
for n in N:
    cnt = 1
    for r in range(1, n // 2 + 1):
        cnt += ncr(n - r, r) * (2 ** r)
    print(cnt)

