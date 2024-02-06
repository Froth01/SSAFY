T = int(input())
primes = [True] * (10001)
primes[0] = primes[1] = False
prime = []
for n in range(2, 10000):
    if primes[n]:
        prime.append(n)
        for i in range(2 * n, 10000, n):
            primes[i] = False
for t in range(T):
    N = int(input())
    S = []
    for p in prime:
        if p<=N-p and primes[N-p]:
            S.append(p)
    print(max(S),N-max(S))

