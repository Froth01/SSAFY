def fac(num):
    nf = num
    if num == 0:
        return 1
    for n in range(1, num):
        nf = nf * (num - n)
    return nf


def ncr(n, r):
    return fac(n) // (fac(n - r) * fac(r))


T = int(input())
for t in range(T):
    N = int(input())
    N //= 10
    cnt = 1
    for r in range(1, N // 2 + 1):
        cnt += ncr(N - r, r) * (2 ** r)
    print(f'#{t + 1} {cnt}')