import math

def efficiency(X, Y, M):
    attack = math.ceil(M / X)
    item_attack = math.ceil(M / (X + Y))
    return attack / item_attack

def find_lowest_efficiency(X, Y, K):
    low_ef = float('inf')
    low_M = None
    for M in range((X+Y),2*K,(X+Y)):
        if M<K:
            continue
        effect = efficiency(X, Y, M)
        if effect < low_ef:
            low_ef = effect
            low_M = M
    for M in range((X+Y)-1,2*K,(X+Y)):
        if M<K:
            continue
        effect = efficiency(X, Y, M)
        if effect < low_ef:
            low_ef = effect
            low_M = M
    for M in range((X+Y)+1,2*K,(X+Y)):
        if M<K:
            continue
        effect = efficiency(X, Y, M)
        if effect < low_ef:
            low_ef = effect
            low_M = M
    return low_M

X, Y, K = map(int, input().split())
print(find_lowest_efficiency(X, Y, K))
